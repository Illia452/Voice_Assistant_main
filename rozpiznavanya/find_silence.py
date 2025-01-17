from pydub import AudioSegment
from pydub.utils import db_to_float
import itertools



# Виклик функції detect_silence

def detect_silence(audio_segment, min_silence_len=1000, silence_thresh=-16, seek_step=1):
    """
    Returns a list of all silent sections [start, end] in milliseconds of audio_segment.
    Inverse of detect_nonsilent()

    audio_segment - the segment to find silence in
    min_silence_len - the minimum length for any silent section
    silence_thresh - the upper bound for how quiet is silent in dFBS
    seek_step - step size for interating over the segment in ms
    """
    seg_len = len(audio_segment)

    # you can't have a silent portion of a sound that is longer than the sound
    if seg_len < min_silence_len:
        return []

    # convert silence threshold to a float value (so we can compare it to rms)
    silence_thresh = db_to_float(silence_thresh) * audio_segment.max_possible_amplitude

    # find silence and add start and end indicies to the to_cut list
    silence_starts = []

    # check successive (1 sec by default) chunk of sound for silence
    # try a chunk at every "seek step" (or every chunk for a seek step == 1)
    last_slice_start = seg_len - min_silence_len
    slice_starts = range(0, last_slice_start + 1, seek_step)

    # guarantee last_slice_start is included in the range
    # to make sure the last portion of the audio is searched
    if last_slice_start % seek_step:
        slice_starts = itertools.chain(slice_starts, [last_slice_start])

    for i in slice_starts:
        audio_slice = audio_segment[i:i + min_silence_len]
        if audio_slice.rms <= silence_thresh:
            silence_starts.append(i)

    # short circuit when there is no silence
    if not silence_starts:
        return []

    # combine the silence we detected into ranges (start ms - end ms)
    silent_ranges = []

    prev_i = silence_starts.pop(0)
    current_range_start = prev_i

    for silence_start_i in silence_starts:
        continuous = (silence_start_i == prev_i + seek_step)

        # sometimes two small blips are enough for one particular slice to be
        # non-silent, despite the silence all running together. Just combine
        # the two overlapping silent ranges.
        silence_has_gap = silence_start_i > (prev_i + min_silence_len)

        if not continuous and silence_has_gap:
            silent_ranges.append([current_range_start,
                                  prev_i + min_silence_len])
            current_range_start = silence_start_i
        prev_i = silence_start_i

    silent_ranges.append([current_range_start,
                          prev_i + min_silence_len])

    return silent_ranges


# silences = detect_silence(audio, min_silence_len=1000, silence_thresh=-50, seek_step=100)

# Вивести знайдені діапазони тиші
# print(f"Found silent sections: {silences}")



"""
while True:
            self.text_vosk_text = self.result.get("text")
            self.text_vosk_partial = self.result.get("partial")

            if len(self.text_vosk_partial) != 0:
                self.text_vosk = self.text_vosk_partial
            else:
                self.text_vosk = self.text_vosk_text

            doc1 = self.nlp(self.text_vosk)
            self.text_vosk.clear()
            self.text_vosk_partial.clear()
            self.text_vosk_text.clear()

            tokens1 = [word.text for sentence in doc1.sentences for word in sentence.words]

            for i in range(len(tokens1)):
                if i < len(self.text_command):
                    similarity = (fuzz.ratio(self.text_command[i], tokens1[i])) 
                    if similarity >= 80: # при умові якщо слова в речені з однаковими індексами мають схожість більше 80% то залишаємо все як є
                        continue   
                    elif similarity <= 79: # якщо ж слово має менше 80% cхожості то замінюємо його з потоку vosk
                        self.text_command[i] = tokens1[i]
                    elif similarity <=60:
                        self.text_command.insert(i+1, tokens1[i]) # якщо ж слово має схожість менше 60%, додаємо це слово поряд
                else:                                               # є шанс що це нова команда
                    for number, item in enumerate(tokens1): # якщо ж кількість слів між потоком vosk та нашим текстом відрізняється...
                        self.text_command.extend(tokens1[len(self.text_command):]) # ...то додаємо кількість слів яка залишилась
            if self.detect == True:
                break
            
            if len(self.text_command) != 0:
                while True:

                    self.list_silence.append(self.str_audio) # додавання фрагментів після підвищення гучності
                    full_audio = sum(self.list_silence) # об'єднання цих фрагментів 
                    self.silence = detect_silence(full_audio, min_silence_len=500, silence_thresh=-50, seek_step=100) # налаштування для функції тиші

                    for silence in self.silence:
                        if (silence[1] - silence[0]) >= 1800:
                            print(f"НАША КОМАНДА: {self.text_command}")
                            self.detect = True
                            break
                            
                    print(f"НАША КОМАНДА: {self.text_command}")
                    return                
            """
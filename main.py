from requests import get

def download(url, file_name):
	try:
		with open(file_name, "wb") as file:   # open in binary mode
			response = get(url)               # get request
			file.write(response.content)      # write to file	
		return True

	except:
		return False


from moviepy.editor import VideoFileClip

def videoToAudio(file_path):
	try:
		video = VideoFileClip(f"{file_path[:-4]}.mp4")
		video.audio.write_audiofile(f"{file_path[:-4]}.wav", codec='pcm_s16le')
		return True

	except:
		return False


import speech_recognition as sr

def writeScript(audio_file_path):
	recognizer = sr.Recognizer() # 음성 인식 객체 생성

	# 음성 파일 불러오기
	with sr.AudioFile(audio_file_path) as source:
		audio_data = recognizer.record(source)

	# Google Web Speech API를 사용하여 음성을 텍스트로 변환
	try:
		text = recognizer.recognize_google(audio_data, language="ko-KR")
		print("인식된 텍스트:", text)
		return True

	except sr.UnknownValueError:
		print("음성을 인식하지 못했습니다.")
		return False

	except sr.RequestError as e:
		print(f"Google Web Speech API 요청 에러: {e}")
		return False


if __name__ == '__main__':
	url = "https://lms.cu.ac.kr/contents/189/7590/2722_720p.mp4"
	# download(url,"./dataset_dir/download.mp4")
	# videoToAudio("./dataset_dir/download.mp4")
	writeScript("./dataset_dir/download.wav")
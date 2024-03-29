import assemblyai as aai
from dotenv import load_dotenv
import os

load_dotenv()

aai.settings.api_key = os.getenv("ASSEMBLYAI_API_KEY")

"""
    To perform real-time transcription, we open a WebSocket with the AssemblyAI servers. 
    A WebSocket is a protocol that keeps a communication channel between a client and server alive, 
    which allows for the server to push data to the client without an explicit request. 
    This ability and the relatively low overhead of WebSockets make them perfectly suitable for real-time data transfer.
    
    
    Every message that AssemblyAI’s server sends is one of two types - either a partial transcript, or a final transcript.
"""


def on_data(transcript: aai.RealtimeTranscript):
  # handle when there is no text
  if not transcript.text:
    return

  if isinstance(transcript, aai.RealtimeFinalTranscript):
    print(transcript.text, end="\r\n")
  else:
    print(transcript.text, end="\r")
    
# Error handler
def on_error(error: aai.RealtimeError):
  print("An error occured:", error)
  
def on_open(session_opened: aai.RealtimeSessionOpened):
  print("Session ID:", session_opened.session_id)

def on_close():
  print("Closing Session")
  
# Create and run the transcriber
## initiate RealtimeTranscriber object
transcriber = aai.RealtimeTranscriber(
  on_data=on_data,
  on_error=on_error,
  sample_rate=44_100,
  on_open=on_open,
  on_close=on_close,
)

## open the WebSocket by using this object’s connect
transcriber.connect()

## Stream audio from the microphone and send it to the WebSocket
microphone_stream = aai.extras.MicrophoneStream()
transcriber.stream(microphone_stream)

## clean up all loose ends
transcriber.close()




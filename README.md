# Project Overview:
RealTimeTranscriber is an application that leverages the AssemblyAI platform to perform real-time transcription of audio input. The application establishes a WebSocket connection with the AssemblyAI servers, enabling seamless communication for receiving audio data and receiving transcription results. This project aims to provide a convenient solution for transcribing audio content in real-time, with applications ranging from live captioning to speech-to-text conversion for accessibility purposes.

## Features:
1. Real-Time Transcription: Utilizes WebSocket communication to receive audio input and transmit transcription results in real-time.
2. Partial and Final Transcripts: Handles both partial and final transcripts received from the AssemblyAI servers, providing continuous updates as transcription progresses.
3. Error Handling: Implements error handling mechanisms to manage and report any errors encountered during the transcription process.
4. Session Management: Manages the WebSocket session, including opening and closing connections as needed.
5. Sample Rate Configuration: Supports customization of the sample rate for audio input, allowing flexibility in handling different types of audio streams.

## Usage:
- Connect to AssemblyAI: Establishes a WebSocket connection with the AssemblyAI servers.
- Stream Audio Input: Streams audio input from the microphone or any compatible audio source.
- Receive Transcription: Receives partial and final transcripts from the AssemblyAI servers and displays them in real-time.
- Error Handling: Handles errors encountered during the transcription process and provides appropriate feedback.
- Close Session: Closes the WebSocket connection and performs cleanup operations upon completion.

## Installation:
Clone the repository to your local machine.
Install the required dependencies using pip install -r requirements.txt.
Set up environment variables, including the AssemblyAI API key, using a .env file.
Run the application script to initiate the RealTimeTranscriber.

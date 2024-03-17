import speech_recognition as sr
import PyPDF2 

# Initialize the recognizer
r = sr.Recognizer()

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

# Use the microphone as the source for input
with sr.Microphone() as source:
    print("Say something:")

    # Adjust for ambient noise
    r.adjust_for_ambient_noise(source)

    # Listen for the user's input
    audio = r.listen(source)

    try:
        # Recognize speech using Google Speech Recognition
        text_from_audio = r.recognize_google(audio)
        print("You said:", text_from_audio)

        # Path to the PDF file
        pdf_path = "/home/jeyasri/Pictures/tax.pdf"
        
        # Extract text from PDF
        pdf_text = extract_text_from_pdf(pdf_path)
        if text_from_audio.lower() in pdf_text.lower():
            print("The recognized text is in the PDF.")
            # Find the paragraph containing the matched text
            paragraphs = pdf_text.split("\n\n")  # Split text into paragraphs
            for paragraph in paragraphs:
                if text_from_audio.lower() in paragraph.lower():
                    print("Matched Paragraph:")
                    print(paragraph)
                    break
        else:
            print("The recognized text is not found in the PDF.")

    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Error occurred during recognition: {}".format(e))

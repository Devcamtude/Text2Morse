from django.shortcuts import render
from .morse_code_converter import text_to_morse

def convert_text_to_morse(request):
    if request.method == 'POST':
        text = request.POST.get('text', '')
        morse_code = text_to_morse(text)
        return render(request, 'converter/converter.html', {'text': text, 'morse_code': morse_code})
    return render(request, 'converter/converter.html')

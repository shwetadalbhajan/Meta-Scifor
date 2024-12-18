from django.shortcuts import render
import yt_dlp
import os

def youtube(request):
    if request.method == 'POST':
        link = request.POST.get('link', '')

        if link:
            try:
                output_path = r'C:\Users\Public\Videos'

                if not os.path.exists(output_path):
                    os.makedirs(output_path)
                ydl_opts = {
                    'format': 'best',
                    'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
                }

                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([link])

                message = "Video downloaded successfully!"
            except Exception as e:
                message = f"Error downloading video: {str(e)}"
        else:
            message = "Please provide a valid link."

        return render(request, 'index.html', {'message': message})
    return render(request, 'index.html')

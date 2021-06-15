from moviepy.editor import *

class AutomaticFilmGen():

    def make_film(self,multi_clips, multi_music, output_path, max_time):
        def arrange_clips(max_time, multi_clips, order):
                video_clips =[]
                end_times = []
                end_times.append(0)
                
                for n in order:
                    clip = VideoFileClip(multi_clips[n])
                    clip_time = clip.duration
                    time = max_time
                    if max_time > clip_time:
                        time = clip_time
                    start=0
                    clip = clip.subclip(start,start+time)
                    clip = clip.set_start(end_times[len(end_times)-1])
                    end_times.append(clip.end)
                    video_clips.append(clip)
                    line = "Clip: " + str(n) + " done\n"
                    print("Clip: " + str(n) + " done\n")
                    
                return video_clips

        def arrange_music(multi_music, order, generated_clips, fadetime):
            #iscut daje losowy przydzial audio
            clips_time = sum(map(float,[f.duration for f in generated_clips]))
            all_music_time = sum([AudioFileClip(f).duration for f in multi_music])
            clips_music = []
            print(clips_time)

            end_times = []
            end_times.append(0)
            

            for n in order:
                music = AudioFileClip(multi_music[n])
                if music.duration > (clips_time-end_times[len(end_times)-1]):
                    music = music.set_start(end_times[len(end_times)-1])
                    music = music.set_end(clips_time)
                    music = music.audio_fadein(fadetime).audio_fadeout(fadetime)
                    clips_music.append(music)
                    break
                else:
                    music = music.set_start(end_times[len(end_times)-1])
                    clips_music.append(music)
                    end_times.append(music.end)
            return clips_music

        clips_order = [n for n in range(0,len(multi_clips))]
        music_order = [n for n in range(0,len(multi_music))]
        generated_clips = arrange_clips(max_time,multi_clips,clips_order)
        line=(">>> Clips generated\n\n")
        print(">>> Clips generated\n\n")

        generated_music = arrange_music(multi_music, music_order, generated_clips, 1.5)
        line=(">>> Music generated\n\n")
        print(">>> Music generated\n\n")


        final = CompositeVideoClip(generated_clips)
        final_audio = CompositeAudioClip(generated_music)
        final = final.set_audio(final_audio)
        line=(">>> Started writing...\n")
        print(">>> Started writing...\n")
        final.write_videofile(output_path)

    


from twitchio.ext import commands
import pafy
import vlc


@commands.cog(name='songrequest')
class songrequest:

    def __init__(self, bot):
        print('Song Request Cog loaded')
        self.bot = bot
        self.songlist = []
        self.url = 'https://www.youtube.com/watch?v=Lx58hXh4pVA'
        # self.url = 'https://github.com/mediaelement/mediaelement-files/blob/master/big_buck_bunny.mp4?raw=true'
        # self.url = 'http://www.hochmuth.com/mp3/Haydn_Cello_Concerto_D-1.mp3'

    @commands.command(name='songrequest', aliases=['sr'])
    async def binding(self, ctx):
        video = pafy.new(self.url)
        best = video.getbest()
        playurl = best.url

        Instance = vlc.Instance()
        player = Instance.media_player_new()
        Media = Instance.media_new(playurl)
        Media.get_mrl()
        player.set_media(Media)
        player.play()


        # id = ctx.message.content.split()[1]
        # media_player = vlc.MediaPlayer(f'{self.url}')
        # media_player.play()
        #https://www.youtube.com/watch?v=Lx58hXh4pVA
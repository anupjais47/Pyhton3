import instaloader
L=instaloader.instaloader()
profile=input("Enter the profile name : ")
L.download_profile(profile,profile_pic_only=True)
# Credit and special thanks to @akshat_gosain for figuring out how to fix.

import random
bsdk = ["Phatele Nirodh Ke Natije!","Chut Ka Maindak…","Abla Naari, Tere Bable Bhaari…","Chut Ke Pasine Mein Talay Hue Bhajiye…","Chullu Bhar Muth Mein Doob Mar!","Kaali Chut Ke Safed Jhaant…","Gote Kitne Bhi Badey Ho, Lund Ke Niche Hi Rehtein Hain…","Naa Chut, Naa Choche, Aur Nakhre Noor Jahan Ke!","Teri Gaand Mein Kutte Ka Lund…","Teri Jhaatein Kaat Kar Tere Mooh Par Laga Kar Unki French Beard Bana Doonga!"]
@ultroid_cmd(pattern="bsdk")
async def thanks(ult):
  b = random.choice(bsdk)
  return await eor(ult, b)
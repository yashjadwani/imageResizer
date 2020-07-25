from PIL import Image

validFormats=['jpg','jpeg','png']
name = input("Image : ")
if (name !='' and len(name.split(".")) != 1):
    print("Leave feilds empty If you don't wish to change")
    height = input("Height : ").strip()
    width = input("width : ").strip()
    quality = input("Quality (in percentage) : ").strip()
    if(name.split(".")[1] in validFormats):
        if (height == '' and width =='' and quality == ''):
            print("No parameter changed!")
        else:
            try:
                image = Image.open(name)
                heightOg,widthOg = image.size
                height = int(height) if height != '' else int(heightOg)
                width = int(width) if width != '' else int(widthOg)
                image = image.resize((height, width), Image.ANTIALIAS)
                image = image.convert('RGB')
                if (quality == ''):
                    image.save(name.split(".")[0]+"_resize."+name.split(".")[1])
                else:
                    image.save(name.split(".")[0] + "_resize."+name.split(".")[1], optimize=True,quality=int(quality))
                print("Saved Succesfully")
            except FileNotFoundError:
                print("No such file or directory: "+name )
            except ValueError as e:
                print("please enter proper values or Leave it as blank")
                print(e)
    else:
        print("Please enter valid file format")
else:
    print("Please enter valid file Name")





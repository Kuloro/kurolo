# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define xx = Character("บรรยาย")
define x = Character("บุคคลปริศนา")
define a = Character("sonari")
define b = Character("yuuki")
define c = Character("kotori")
define me = Character("[name]")
define sensei = Character("อาจารย์")




# The game starts here.

label start:

    $ renpy.movie_cutscene('opensakura.avi')
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    $ a_point = 5
    $ b_point = 1
    $ c_point = 1
    $ t_point = 1



    scene school

    xx "วันนี้เป็นวันแรกของคุณในรรนี้"
    xx "โรงเรียนนี้ชื่อว่าชากุระวิทยาลัย"
    xx "เป็นโรงเรียนประจำจังหวัดของที่นี่"
    xx "และเหตุผลที่ต้องมาเข้าเรียนกลางเทอมเพราะคุณพึ่งย้ายมาจากต่างจังหวัด"

    

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show yuuki at right :
        zoom 2


    # These display lines of dialogue.
    play sound "audio/a1.wav"


    x "สวัสดีนักเรียนใหม่นายมาโรงเรียนนี้ครั้งแรกสินะ"
    

    play sound "audio/a2.wav"

    x "แล้วนายชื่ออะไรละ"

    $ name = renpy.input("กรอกชื่อของคุณ(แนะนำให้เขียนภาษาไทย)")
    $ name = name.strip()
    # This ends the game.

    play sound "audio/a3.wav"


    x "[name]งั้นหรอเป็นชื่อที่ดีนะ"


    play sound "audio/a5.wav"

    x "ขอให้โชคดีกับรั่วโรงเรียนใหม่"


    menu:
        "เธอช่วยพาฉันไปดูรอบโรงเรียนได้ไหม":
            jump a
            $ a_point += 1

        "อืมโชคดีไว้เจอกันนะ":
            jump b

        "ฉันยังไม่ได้ถามชื่อเธอเลย":
            jump c
            $ a_point += 1

    label a:

        me "เธอช่วยพาฉันไปดูรอบโรงเรียนได้ไหม"

        play sound "audio/a4.wav"

        x "ได้สิเดี๋ยวฉันจะพาไป"

        scene sakura
        
        play sound "audio/a6.wav"
        x "ที่นี่คือต้นชากุระประจำโรงเรียน"

        play sound "audio/a7.wav"

    
        x "นอกจากจะเป็นสถานที่สำคัญของโรงเรียนแล้วยังเป็นที่ๆคนชอบมาขอพรเกี่ยวกับความรักด้วย"

        play sound "audio/a8.wav"

        x "ถ้าเกิดนายเกิดเป็นกังวลละก็ลองมานั่งแถวนี้ได้มันทำให้สงบสติอารมณ์ได้เยอะเลย"

        scene ss:
            zoom 1.5

        play sound "audio/a9.wav"

        x "ต่อไปเป็นสวนสาธารณะที่นี่จะคนเยอะตอนพักกลางวัน"
        
        play sound "audio/a10.wav"

        x "ก็อย่างที่เห็นไม่มีอะไรมากหรอก"

        scene up

        play sound "audio/a11.wav"

        x "ที่นี่คือด่านฟ้าของอาคารเรียน"

        play sound "audio/a12.wav"

        x "อาคารนี่เป็นอาคารเดียวที่ขึ้นด่านฟ้าได้่"

        play sound "audio/a13.wav"

        x "ที่นี่ทั้งวิวสวยแล้วก็ลมเย็นด้วย แต่ต้องระวังให้ดีเพราะที่นี่ไม่ได้ถูกอนุญาตุให้ขึ้นหรอกนะ"

        scene lib:
            zoom 2


        play sound "audio/a14.wav"

        x "ที่นี่คือห้องสมุดโดยปกติแล้วฉันมักจะอยู่ที่นี่เวลาว่างนะ"

        play sound "audio/a19.wav"

        x "อ่อแล้วชื่อของฉันคือยูกิ"
        
        play sound "audio/a18.wav"

        b "ถ้าเกิดนายไม่มีเพื่อนก็แวะมาเล่นด้วยกันได้นะ"

        menu:
            "ได้สิไว้จะมานะ":
                jump aa
                $ a_point += 2

            "ถ้าเกิดสายลมชี้ทางละก็นะ":
                jump aa
                $ a_point += 1
                $ c_point += 1


            "จะเก็บไปคิดแล้วกัน":
                jump aa
                $ a_point += 0
                $ b_point += 1


    label c:
        me "ฉันยังไม่ได้ถามชื่อเธอเลย"

        play sound "audio/a15.wav"


        x "ฉันชื่อ yuuki ยินดีที่ได้รู้จักนะ"

        play sound "audio/a16.wav"


        b "เอางี้ไหมละเดี๋ยวฉันจะพานายเดินชมโรงเรียนเอง"

        me "เอาสิ"


        scene sakura
        
        play sound "audio/a6.wav"
        b "ที่นี่คือต้นชากุระประจำโรงเรียน"

        play sound "audio/a7.wav"

    
        b "นอกจากจะเป็นสถานที่สำคัญของโรงเรียนแล้วยังเป็นที่ๆคนชอบมาขอพรเกี่ยวกับความรักด้วย"

        play sound "audio/a8.wav"

        b "ถ้าเกิดนายเกิดเป็นกังวลละก็ลองมานั่งแถวนี้ได้มันทำให้สงบสติอารมณ์ได้เยอะเลย"

        scene ss:
            zoom 1.5

        play sound "audio/a9.wav"

        b "ต่อไปเป็นสวนสาธารณะที่นี่จะคนเยอะตอนพักกลางวัน"
        
        play sound "audio/a10.wav"

        b "ก็อย่างที่เห็นไม่มีอะไรมากหรอก"

        scene up

        play sound "audio/a11.wav"

        b "ที่นี่คือด่านฟ้าของอาคารเรียน"

        play sound "audio/a12.wav"

        b "อาคารนี่เป็นอาคารเดียวที่ขึ้นด่านฟ้าได้่"

        play sound "audio/a13.wav"

        b "ที่นี่ทั้งวิวสวยแล้วก็ลมเย็นด้วย แต่ต้องระวังให้ดีเพราะที่นี่ไม่ได้ถูกอนุญาตุให้ขึ้นหรอกนะ"

        scene lib:
            zoom 2


        play sound "audio/a14.wav"

        b "ที่นี่คือห้องสมุดโดยปกติแล้วฉันมักจะอยู่ที่นี่เวลาว่างนะ"

        play sound "audio/a18.wav"


        b "ถ้าเกิดนายไม่มีเพื่อนก็แวะมาเล่นได้นะ"
    

        jump aa


    label b :

        play sound "audio/a17.wav"


        x "โอเค ฉันชื่อyuuki นะถ้าเจอกันครั้งหน้าก็ทักทายกันด้วยละ"

        jump aa

    label aa:

        scene way :
            zoom 2

        me "ต่อไปนี้ ที่นี่ต่อห้องเรียนของฉันสินะ เอาละ"

        sensei "เอาละนักเรียนใหม่เข้ามาได้"

        scene class:
            zoom 2

        sensei "แนะนำตัวชะ"


        menu:
            "ฉันชื่อ [name] ขอฝากตัวด้วยนะ":
                jump ba
                $ a_point += 1

            "ข้ามีนามว่า [name] บุตรแห่งความมืดเป็นผู้ที่จะมายึดครองโรงเรียนนี้ยังไงละ":
                jump ba
                $ a_point -= 1
                $ c_point += 1

            "ฉันชื่อ [name] ถ้าเป็นไปได้ก็ช่วยอย่ามายุ่งกับฉันมากละ":
                jump ba
                $ a_point -= 2
                $ b_point += 1


        

    label ba:

        scene class:
            zoom 2

        sensei "งั้นนายไปนั่งข้าง yuuki นะ"

        show yuuki:
            zoom 2

        play sound "audio/a20.wav"

        
        b "ไง บังเอิญจังนะที่ได้มาอยู่ห้องเดียวกัน"

        menu:
            "นั้นสินะบังเอิญจังนะ":
                jump baa
                $ a_point += 1

            "ฉันว่ามันเป็นโชคชะตามากกว่านะ":
                jump bab
                $ a_point += 1
                $ c_point += 1

            "ถ้าเป็นไปได้ก็ไม่อยากเจอหรอก":
                jump bac 
                $ a_point -= 2
                $ b_point += 1


    label baa:

        scene class:
            zoom 2

        sensei "เอาละถึงเวลาพักเที่ยงแล้วเลิกคลาสได้"

        xx "พักเที่ยงคุณจะไปกินข้าวที่ไหน"

        menu:
            "โรงอาหาร":
                jump baaa
            "ห้องสมุด":
                jump baab
            "ด่านฟ้า":
                jump baac
                $ b_point += 1


    label baaa:
        scene luch

        me "ที่นี่คนเยอะจังเลยแหะมาคนเดียวคงไม่เหมาะ"

        me "เปลี่ยนไปกินที่อื่นดีกว่า"


        menu:

            "ห้องสมุด":
                jump baab
            "ด่านฟ้า":
                jump baac
                $ b_point += 1



    label baab:

        scene lib:
            zoom 2

        show yuuki at right:
            zoom 2

        play sound "audio/a21.wav"

        b "เอ้า[name]นี่นามากินข้าวด้วยกันสิ"

        xx "คุณได้เข้าไปอยู่ในกลุ่มเพื่อนของyuuki"

        xx "แม้คุณจะอึดอัดอยู่บ้างแต่ก็ดีกว่ากินคนเดียวในโรงอาหาร"

        jump classwork

    label baac:

        scene up

        me "ที่นี่คือด่านฟ้าสินะดูสงบดีจังเลย"

        play sound "audio/b1.wav"

        

        x "ฉันว่านายไม่ควรมาที่นี่หรอกนะ"

        scene sonaricut

        scene up

        show sonari at right:
            zoom 2

        play sound "audio/b2.wav"

        x "เด็กใหม่อย่างนายควรไปกินข้าวกับเพื่อนใหม่สิถึงจะถูก"

        play sound "audio/b3.wav"

        x "ฉันแนะนำให้นายไปที่ห้องสมุดเพราะyuukiอยู่ที่นั้น"

        jump baab


    label bab:
        
        scene class:
            zoom 2

        sensei "เอาละถึงเวลาพักเที่ยงแล้วเลิกคลาสได้"

        xx "พักเที่ยงคุณจะไปกินข้าวที่ไหน"

        menu:
            "โรงอาหาร":
                jump baba
            "ห้องสมุด":
                jump babb
            "ด่านฟ้า":
                jump babc
                $ b_point += 1


    label baba:
        scene luch

        me "ที่นี่คนเยอะจังเลยแหะมาคนเดียวคงไม่เหมาะ"

        me "เปลี่ยนไปกินที่อื่นดีกว่า"


        menu:

            "ห้องสมุด":
                jump babb
            "ด่านฟ้า":
                jump babc
                $ b_point += 1


    label babb:

        scene lib:
            zoom 2
        show yuuki at right:
            zoom 1.5

        play sound "audio/a21.wav"

        b "เอ้า[name]ผู้ยืดครองโรงเรียนนี่นานี่นามากินข้าวด้วยกันสิ"

        xx "คุณได้เข้าไปอยู่ในกลุ่มเพื่อนของyuuki"

        xx "คุณรู้สึกอึดอัดมากเนื่องจากพวกเขาชอบล้อคุณ"

        jump classwork

    label babc:

        scene up

        me "ที่นี่คือด่านฟ้าสินะดูสงบดีจังเลย"

        play sound "audio/b1.wav"

        x "ฉันว่านายไม่ควรมาที่นี่หรอกนะ"

        scene sonaricut

        scene up

        show sonari at right:
            zoom 2

        play sound "audio/b2.wav"

        x "เด็กใหม่อย่างนายควรไปกินข้าวกับเพื่อนใหม่สิถึงจะถูก"

        play sound "audio/b3.wav"

        x "ฉันแนะนำให้นายไปที่ห้องสมุดเพราะyuukiอยู่ที่นั้น"

        jump babb

    label bac:

        scene class:
            zoom 2

        sensei "เอาละถึงเวลาพักเที่ยงแล้วเลิกคลาสได้"

        xx "พักเที่ยงคุณจะไปกินข้าวที่ไหน"

        menu:
            "โรงอาหาร":
                jump baca
            "ห้องสมุด":
                jump bacb
            "ด่านฟ้า":
                jump bacc
                $ b_point += 1

    
    label baca:
        scene luch

        me "ที่นี่คนเยอะจังเลยแหะมาคนเดียวคงไม่เหมาะ"

        me "เปลี่ยนไปกินที่อื่นดีกว่า"


        menu:

            "ห้องสมุด":
                jump bacb
            "ด่านฟ้า":
                jump bacc
                $ b_point += 1


    label bacb :

        scene lib:
            zoom 2

        show yuuki at right:
            zoom 2

        play sound "audio/a22.wav"

        b "ไหนว่าไม่อยากเจอฉันไงแล้วมาทำไมที่นี่ละ"

        xx "คุณโดนyuukiไล่อย่างไม่ปราณี"

        xx "คุณรู้สึกอึดอัดมากจึงต้องออกไป"

        jump classwork


    label bacc:

        scene up

        me "ที่นี่คือด่านฟ้าสินะดูสงบดีจังเลย"

        play sound "audio/b4.wav"

        x "เด็กใหม่นายเองหรอ"

        scene sonaricut

        scene up

        show sonari at right:
            zoom 2

        play sound "audio/b5.wav"

        x "นายนะไม่ควรพูดอย่างงั้นกับyuukiตั้งแต่แรกเพราะเธอเป็นศูนย์กลางของห้อง"

        play sound "audio/b6.wav"

        x "ฉันว่านายคงจะถูกเกลียดเข้าแล้วละ เด็ก-ใหม่"

        menu:
            "ทำไมคิดว่างั้นละ":
                jump babca
                $ b_point += 1

            "จริงๆฉันก็เกลียดเธอเหมือนกัน":
                jump babcb
                $ a_point -= 2


    label babca:

        scene up

        show sonari at right:
            zoom 2
        play sound "audio/b7.wav"
        x "เพราะว่านี้คือสถานที่แบบนั้นนะสิ"

        jump claswork

    
    label babcb:

        scene up

        show sonari at right:
            zoom 2

        play sound "audio/b8.wav"

        x "หรอ งั้นก็อยู่เงียบๆละกัน"

        jump claswork

    label classwork:

        scene class:
            zoom 2

        $ t_point += 1

        xx "วันต่อมา"

        xx "วันนี้ก็เป็นอีกวันในโรงเรียน"

        xx "คุณยังคงนั่งเรียน"

        xx "จนเสียงอ้อดดังขึ้น"


        xx "ถึงเวลาพักเที่ยงแล้วคุณจะไปกินข้าวที่ไหน"

        menu:
            "โรงอาหาร":
                jump luch


            "ห้องสมุด":
                $ a_point += 1
                jump libb
                

            "ด่านฟ้า":
                $ b_point += 1
                jump up
                

    label luch:
        scene luch


        if c_point == 5 :
            
            play sound "audio/c1.wav"

            x "เห้ เจ้าหนะ ข้าหมายถึงเจ้านั้นแหละ"

            scene luch

            show kotori at right:
                zoom 2
            play sound "audio/c2.wav"

            c "นามของข้าคือ kotori ผู้เกิดจากความมืดและช่อนในความมืด"
            play sound "audio/c3.wav"

            c "บุตรแห่งความมืดเอ้ยจงมาร่วมมือกับข้าแล้วยืดครองโรงเรียนนี้ไปด้วยกันเถอะ"

            menu:
                "เมิน" :
                    $ c_point -= 5
                    jump classwork

                "ได้สิแต่ว่า เจ้าพร้อมแล้วสินะที่จะทำสัญญาแห่งความมืดกับข้า":
                    $ c_point += 5
            play sound "audio/c4.wav"

            c "ฮะ ฮะ ฮะ แน่นอนอยู่แล้ว"

            sensei "พวกเธอนะอย่าเสียงดังในโรงอาหาร"
            xx "คุณโดนไล่ออกไป"
            jump classwork



        else :
            if c_point == 10 :

                scene luch
                $ c_point += 5
                show kotori at right:
                        zoom 1.5
                
                play sound "audio/c5.wav"

                c "เอาละผู้ทำสัญญากับข้าวันนี้เรามาหาลือเรื่องยึดครองโรงเรียนกันเถอะ"
                xx "คุณได้คุยเล่นกัน kotori จนหมดเวลาพักเที่ยง"

                jump classwork
            else :
                if c_point == 15 :
                    scene luch

                    show kotori at right:
                        zoom 1.5
                    
                    play sound "audio/c6.wav"
                    c "ด้วยนามของข้าkotori เย็นนี้เจ้าจงมาชมเมืองด้วยกันกับข้าชะ"
                    menu :
                        "เอาสิข้าจะไปกับเจ้าเอง":
                            $ c_point += 4
                            xx "หลังจากเลิกเรียนกุก็ได้ไปกับkotori"
                            jump  kotoridate
                    
                        "ไม่เอาอะ":
                            $ c_point -= 10
                            xx "หลังจากนั้นkotoriก็ลุกหนีไป"
                            jump  classwork
                    
                else:   
                    if c_point == 20 :    
                        $ renpy.movie_cutscene('kotoricut.avi')
                        scene luch

                        show kotori at right:
                            zoom 1.5
                        menu:
                            "วันนี้เธอดูสวยกว่าทุกทีนะ":
                        
                                play sound "audio/c7.wav"
                                c "หึแน่นอนอยู่แล้ว"
                                $ c_point +=  3
                                jump classwork
                                
                        
                            "ไว้คราวหน้าเราไปเที่ยวกันอีกไหม":
                                play sound "audio/c8.wav"
                                c "ไม่ใช่เที่ยวนะไปลาตเวนต่างหาก"
                                $ c_point +=  2
                                jump classwork
                        
                            "คบกับฉํนไหม":
                                if a_point == 20 :
                                    play sound "audio/c9.wav"
                                    c "เดี๋ยวสิ พูดอะไรของเจ้านะมันยังเร็วไปนะ"
                                    jump classwork
                                else :
                                    play sound "audio/c10.wav"
                                    c "ก็เอาสิข้าจะยอมลดตัวไปคบด้วย"
                                    $ c_point +=  100
                                    jump classwork
                    else:               
                        if c_point > 100:
                            $ renpy.movie_cutscene('kotoricut.avi')
                            scene luch

                            show kotori at right:
                                zoom 1.5
                            menu:
                                "วันนี้เธอดูสวยกว่าทุกทีนะ":
                            
                                    play sound "audio/c7.wav"
                                    c "หึแน่นอนอยู่แล้ว"
                                    $ c_point +=  3
                                    jump classwork
                                    
                            
                                "ไว้คราวหน้าเราไปเที่ยวกันอีกไหม":
                                    play sound "audio/c8.wav"
                                    c "ไม่ใช่เที่ยวนะไปลาตเวนต่างหาก"
                                    $ c_point +=  2
                                    jump classwork    
                            
                        else:

                            xx "ที่นี่คนเยอะคงไม่เหมาะกับการกินคนเดียว"
                            menu:
                                "เลือกที่จะอยู่":
                                    $ c_point += 1


                                "ไปห้องสมุด":
                                    jump libb
                                    $ a_point += 1

                                "ไปด่านฟ้า":
                                    jump up
                                    $ b_point += 1

                            xx "คุณตัดสินใจเลือกกินข้าวคนเดียวที่นี่"
                            xx "หลังจากกินข้าวเสร็จก็กลับไปเรียนต่อ"

                            jump classwork

         



    label libb:

        scene lib:
            zoom 2

        xx "แม้ห้องสมุดของที่นี่จะอนุญาตุให้นำอาหารเข้ามากินได้แต่ก็มีคนไม่มากนักที่จะเอาเข้ามา"

        if a_point == 5 :
            show yuuki at right:
                zoom 2
            
            play sound "audio/a23.wav"

            a "สวัสดีดี[name]มากินข้าวด้วยกันสิ"

            xx "คุณได้กินข้าวกับกลุ่มเพื่อนของยูกิจนหมดเวลาพัก"

            $  a_point += 3
            jump classwork
          

        else:
            
            if a_point == 10 :
        
                show yuuki at right:
                    zoom 2
                
                play sound "audio/a24.wav"

                a "นี่เย็นนี้นายว่างไหม เราไปเที่ยวห้างกันเถอะ"

                menu:
                    "ว่างสิ":
                        xx "หลังจากนั้นเลิกเรียนคุณก็ได้ไปกับเธอ"
                        $ a_point +=  5
                        jump dateyuuki
                        

                    "โทดทีนะฉันไม่ว่าง":
                        $ a_point -=  1
                
                play sound "audio/a25.wav"
                a "โอเคไม่เป็นไรไว้คราวหน้านะ"
                jump classwork
            else:
                if a_point == 13 :
                    $ renpy.movie_cutscene('yuukicut.avi')

                    show yuuki at right:
                        zoom 2
                    
                    menu :
                        "วันนี้เธอดูสวยกว่าทุกทีนะ":
                            play sound "audio/a26.wav"
                            a "งั้นหรอขอบคุณที่ชมนะ"
                            $ a_point +=  3
                            jump classwork
                            
                    
                        "ไว้คราวหน้าเราไปเที่ยวกันอีกไหม":
                    
                            play sound "audio/a27.wav"
                            a "ได้สิ ไว้คราวหน้าไปด้วยกันอีกนะ"
                            $ a_point +=  3
                            jump classwork
                            
                    
                        "คบกับฉํนไหม":
                            if a_point < 20 :
                                play sound "audio/a28.wav"
                                a "หาจู่ๆนายพูดอะไรของนายเนี่ย ฉันว่ามันออกจะกระทันหันไปหน่อยนะ"
                                jump classwork
                            else:
                                if t_point > 15  :
                                    play sound "audio/a29.wav"
                                    a  "โทดทีนะฉันมีแฟนแล้วนะ"
                                else :
                                    play sound "audio/a30.wav"
                                    a "ได้สิ"
                                    xx "คุณได้คบกับyuuki"
                                    $ a_point +=  100
                                    jump classwork
                else:
                    if a_point == 20 :
                        $ renpy.movie_cutscene('yuuki.avi')

                        show yuuki at right:
                            zoom 2
                        
                        menu :
                            "วันนี้เธอดูสวยกว่าทุกทีนะ":
                                play sound "audio/a26.wav"
                                a "งั้นหรอขอบคุณที่ชมนะ"
                                $ a_point +=  3
                                jump classwork
                                
                        
                            "ไว้คราวหน้าเราไปเที่ยวกันอีกไหม":
                                play sound "audio/a27.wav"
                                a "ได้สิ ไว้คราวหน้าไปด้วยกันอีกนะ"
                                $ a_point +=  3
                                jump classwork
                                
                        
                            "คบกับฉํนไหม":
                                if a_point < 20 :
                                    play sound "audio/a28.wav"
                                    a "หาจู่ๆนายพูดอะไรของนายเนี่ย ฉันว่ามันออกจะกระทันหันไปหน่อยนะ"
                                    jump classwork
                                else:
                                    if t_point > 15  :
                                        play sound "audio/a29.wav"
                                        a  "โทดทีนะฉันมีแฟนแล้วนะ"
                                    else :
                                        play sound "audio/a30.wav"
                                        a "ได้สิ"
                                        xx "คุณได้คบกับyuuki"
                                        $ a_point +=  100
                                        jump classwork
                    else :
                        if a_point > 100 :
                            $ renpy.movie_cutscene('yuuki.avi')

                            show yuuki at right:
                                zoom 2
                            play sound "audio/a31.wav"
                            a  "[name] มาแล้วหรอมานี้สิ"
                            xx "คุณได้นั่งกินข้าวกันสองคนจนทำให้คนรอบข้างอิจฉา"
                            
                            menu :
                                "วันนี้เธอดูสวยกว่าทุกทีนะ":
                                    play sound "audio/a26.wav"
                                    a "งั้นหรอขอบคุณที่ชมนะ"
                                    $ a_point +=  2
                                    jump classwork
                                    
                            
                                "ไว้คราวหน้าเราไปเที่ยวกันอีกไหม":
                            
                                    play sound "audio/a27.wav"
                                    a "ได้สิ ไว้คราวหน้าไปด้วยกันอีกนะ"
                                    $ a_point +=  3
                                    jump classwork
                                    
                        else :
                    
                            xx "คุณได้นั่งกินข้าวคนเดียวในห้องสมุด"
                            xx "จากนั้นก็ได้กลับห้องเรียน"
                            jump classwork

    label up:
        scene up
        xx  "ที่นี่ยังสงบและสบายเหมือนเดิม"
        if b_point == 5 :
            show sonari at right:
                zoom 1.5
            
            play sound "audio/b9.wav"
            b "นายยังมาที่นี่อีกหรอ ทำไมไม่ไปหาเพื่อนชะละ"
            menu:
                "งั้นถ้าฉันบอกว่าอยากเป็นเพื่อนกันเธอละ":
                    $ b_point += 5 
                "ชั่งฉันสิ":
                    xx "คุณได้กินข้าวคนเดียวต่อไป"
                    $ b_point -= 5
                    jump classwork
                     
            play sound "audio/b10.wav"
            b "อยากเป็นเพื่อนกับฉันงั้นหรอ ไม่คิดว่าจะได้ยินคำนี้นะเนี้ย"
            xx "หลังจากนั้นคุณก็คุยกับเธอนิดหน่อย"
            jump class
        else:

            if b_point == 10 :
        
                show sonari at right:
                    zoom 1.5
                
                play sound "audio/b11.wav"
                b "นี่นายบอกว่าอยากเป็นเพื่อนกับฉันใช่ไหมงั้นเลิกเรียนช่วยมากับฉันหน่อยจะได้ไหม" 
                menu :
                    "ได้อยู่แล้ว":
                        xx "หลังจากนั้นเลิกเรียนคุณก็ได้ไปกับเธอ"
                        $ b_point += 10
                        jump datesonari
                        

                    "ไม่เอาอะ":
                        $ b_point -= 10 
                
                        play sound "audio/b12.wav"
                        b "งั้นหรอฉันคงมองนายผิดไป"
            else:
                if b_point == 20 :
                    $ renpy.movie_cutscene('sonari.avi')

                    show sonari at right:
                        zoom 2
                    
                    menu :
                        "วันนี้เธอดูสวยกว่าทุกทีนะ":
                            play sound "audio/b13.wav"
                            b "ตาบ้าพูดอะไรออกมาเนี้ย"
                            $ b_point +=  2
                            jump classwork
                            
                    
                        "ไว้คราวหน้าเราไปเที่ยวกันอีกไหม":
                    
                            play sound "audio/ab13.wav"
                            b "ได้สิ ไว้คราวหน้าไปด้วยกันอีกนะ"
                            $ b_point +=  3
                            jump classwork
                            
                        "คบกับฉํนไหม":
                            if b_point < 20 :
                                play sound "audio/b15.wav"
                                b "หาจู่ๆนายพูดอะไรของนายเนี่ย บ้าไปแล้วหรอ"
                                jump classwork
                            else:
                                play sound "audio/b16.wav"
                                b "ถ้าเป็นนายละก็ได้สิ"
                else:
                    if b_point == 20 :
                        $ renpy.movie_cutscene('sonari.avi')

                        show sonari at right:
                            zoom 2
                        
                        menu :
                            "วันนี้เธอดูสวยกว่าทุกทีนะ":
                                play sound "audio/b13.wav"
                                b "ตาบ้าพูดอะไรออกมาเนี้ย"
                                $ b_point +=  2
                                jump classwork
                                
                        
                            "ไว้คราวหน้าเราไปเที่ยวกันอีกไหม":
                                play sound "audio/ab13.wav"
                                b "ได้สิ ไว้คราวหน้าไปด้วยกันอีกนะ"
                                $ b_point +=  3
                                jump classwork
                                
                    else :
                        xx "คุณได้กินข้าวคนเดียวจนหมดเวลาพักเที่ยงจากนั้นก็กลับห้อง"
                        jump classwork
    label kotoridate :
        xx "เป็ยเดทที่สนุกมาก"
        jump classwork
    label yuukidate :
        xx "เป็ยเดทที่สนุกมาก"
        jump classwork
    label sonaridate :
        xx "เป็ยเดทที่สนุกมาก"
        jump classwork
    


return

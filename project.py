import streamlit as st
st.set_page_config(
    page_title="Srishti's Writings",
    layout='centered',
    initial_sidebar_state='expanded',
    
)

# Function to display the main page content
def main_page():
    st.title("Welcome to *The Other Side* 🌎")
    st.header("अंतः अस्ति प्रारंभः❤️🧿")
    st.subheader("About Me")
    st.divider()
    
    col = st.columns(2)
    cont1 = col[0].container()
    cont2 = col[1].container()
    cont1.image('https://4kwallpapers.com/images/wallpapers/lofi-girl-reading-2560x2560-14889.jpg', width=300)
    
    html_code = """
    <h1 style='font-size:20px;'>
      I read, I write, and I love with vigor and hope. My soul belongs to words and books. Everytime I read, I am home. I am here to share my thoughts with you, they shall travel either through my own words or through my perception of other's words.
    </h1>
    <p style='font-size:15px;'>
      ~ Srishti
    </p>
    """
    cont2.write(html_code, unsafe_allow_html=True)
    st.divider()
    #Gallery

    



# Function to display the book review page content
def book_reviews():
    col = st.columns(2)
    cont3 = col[0].container()
    cont4 = col[1].container()
    cont3.subheader("An Ode to Books")
    cont3.write("What a miracle it is that out of these small, flat, rigid squares of paper unfolds world after world after world, worlds that sing to you, comfort and quiet or excite you. Books help us understand who we are and how we are to behave. They show us what community and friendship mean; they show us how to live and die.")
    cont4.image('https://static1.squarespace.com/static/5f13643bd87ba32558d653e7/t/646fa0796a95c12d9656721a/1685037177446/sabina-sturzu-pAk7WnfquaI-unsplash.jpg?format=1500w', width=300)
    html_code = """
    <h1 style='font-size:30px;'>
      Reviews :
    """
    st.write (html_code,unsafe_allow_html=True)
    container = st.container(border=True, height=600)
    container.subheader("Her Last Wish by Ajay K Pandey")
    container.divider()
#img ='C:/Users/user/OneDrive/Desktop/DataScience/Streamlit_library/Capture.PNG'
#container.image(img)
    container.image("https://m.media-amazon.com/images/I/61Svr3ZG4gL._AC_UF1000,1000_QL80_.jpg")
    with st.expander("Click here to read"):
        html_code = """
        <h1 style='font-size:16px;'>
        My opinions have changed on various things after reading this book, may it be love, life, or death. When I got this book, I didn't have many expectations from it. I was never a fan of Indian romance novelists, but I still gave the book a try, and after reading two pages, I knew I was up for a long journey. It was an emotional roller coaster where each character was trying to continue in their life, running away from their miseries and making peace with their problems instead of facing them until ‘HIV’ happened.It is an unusual journey of sacred love, which may seem quite unrealistic for people, and it is always your choice to believe in it or not. This book glorifies love as the purest of all emotions. If you love someone, your actions show that. Sometimes death teaches you how to live, and that statement fits the book perfectly. No one is born perfect; you may be ten, but you too may have insecurities. A call from the hospital stated Mrs. Aastha Sharma's blood has been diagnosed positive for HIV, changing the entire life of a not-so-common man, Vijay Sharma. Vijay was an utterly underconfident, obedient, and introverted middle-class man who left no stone unturned to save his dying wife. His love for his wife knows no boundaries; he knows he can't see his best friend, his love, and his only source of happiness moving away from him; he can't find it in himself to let her beautiful smile and enchanting aura fade away. He decides to accomplish his wife's impossible wishes. For the world, Aastha and Vijay may be two opposite poles with their completely different personalities, but for me, they were two missing pieces of a beautiful puzzle called life!"Her last wish" not only witnesses the beautiful love story between the husband and wife, but it also holds a plethora of life lessons. The beauty of every relationship, may it be with family, friends, or colleagues, is that your family will stand by your side forever. Your parents may expect a lot from you, and you may fail to meet their expectations, but you can never be a failure to them; you will be their most cherished treasure. Your partner may not be perfect, but as long as you know they will hold your hand when death is just steps away from you, you know you are content with whatever you have.Love is the strongest weapon. It gives you all the courage and strength to fight against all odds. It gives you inner peace that even when your whole world is falling apart, you have them by your side. This book taught me that the world is not as bad as we think. The sole reason that the world continues to exist is compassion, and deep down, it is still alive in the hearts of people. Kudos to the author, Mr. Ajay K. Pandey, for doing an amazing job of enlightening the general public on a disease that is still seen as taboo in our country. The pain that HIV or AIDS patients as well as their families go through, along with the social discrimination they face, makes me ashamed to call myself a part of "modern progressive society." For me, "Her last wish" is an ode to life. It is a journey where you will learn to appreciate the beauty of life. Life will never be an easy walk. Every day you go through miseries and sufferings, facing an unjust world, but at the end of the day, returning to a bunch of people who bring a smile to your face is worth it. You are happy that you made it through!




        """
        st.write (html_code,unsafe_allow_html=True)
        
    container = st.container(border=True, height=500)
    container.subheader("Verity By Colleen Hoover")
    container.divider()
    container.image("https://5.imimg.com/data5/SELLER/Default/2023/3/FU/BL/FK/147952517/verity-by-colleen-hoover.jpeg")
    with st.expander("Click here to read"):
        html_code = """
        <h1 style='font-size:16px;'>
        Hooked, Stunned, Appalled!!
        Colleen Hoover's Verity is not just a book, it's an experience in itself. I'm not someone who skims through the book real quick but believe me when I say this, I completed the book on my five-hour flight. Not many, but I have read thrillers before and this book is not just about it.This book left me questioning myself on so many levels. From opening the first page to reading the last chapter, the urge to shut the book and pretend, I never read that was continuously hanging over my head. I was intrigued by the characters, be it Lowen, Verity, Jeremy, or Crew, every character of the book speaks to you at some point. Verity made me believe that I was always right about what it takes to be an author, to be able to write what reaches the hearts of the readers, tears through their flesh, and stays there until every ounce of blood seeps through it. Watching Jeremy from Verity's POV and then watching him through the eyes of Lowen was yet another beauty of this book which I appreciate.
        Hoover did an amazing job as a writer, stepping out of the comfort of writing a romance where readers are left grieving over the love and loss, to switching to a plot where the reader will be left bewildered is definitely not an easy task. The plot twists, the writing style, the ending note after each chapter, everything was so overwhelming. More than the question, "Who was the real villain?", Verity to me will always be about storytelling. Reading the manuscript, then switching again to the present and watching the person live, still prickles my skin. The entire time I was reading the book, some unknown fear continued to grip my heart, anticipating something bad after every line. Hoover's way of taking the readers through the disturbing minds of the characters left me in awe of her writing.
        Its what you do when youve experienced the worst of the worst. You seek out people like you, people worse off than you, and you use them to make yourself feel better about the terrible things that have happened to you.” This abstract from the book continues to haunt me because deep down I know this is the truth, my reality. No matter, whether you like thrillers or not! No matter, if you think Hoover's writing is overrated! Do give this book a chance to let you delve into the universe of grief, sorrow, tragedy, suspense, lies, and above all obsession.




        """
        st.write (html_code,unsafe_allow_html=True)

# Function to display the my writings page content
def my_writings():
    
    html_code = """
    <h1 style='font-size:30px;'>
      My Writings :
    """
    st.write (html_code,unsafe_allow_html=True)
    container = st.container(border=True, height=500)
    container.subheader("कितनी कहानियां")
    container.divider()
    container.image("https://i0.wp.com/picjumbo.com/wp-content/uploads/long-road-in-forest-vertical.jpg?w=2210&quality=70")
    with st.expander("Click here to read"):
        html_code = """
        <h1 style='font-size:16px;'>
        इतनी कहानियां हैं सुनने को तुमसे
        पर फिर यह मौन भी सुंदर लगता है तुम्हारा
        अच्छा छोड़ो! तुम कुछ मेरी सुन लो,
        पर फिर लगता है ,नहीं! खामोशी ही ठीक है

        अगर कहानियां सुन कर दूर हो गई 
        वो नाराजगी भी , फिर?
        गलतफहमी के ही सही,
        किसी रिश्ते से तो जुड़े हो तुम मुझसे!

        अगर यह गलत फहमियां भी खत्म हो गई
        फिर अनजान हो जायेंगे हम दोनो।
        फिर क्या देखोगे तुम मेरी तरफ दुबारा कभी?
        क्या टकराएंगे हमारे रास्ते फिर कहीं?
        नथुने फुलाकर ही सही, पर 
        एक नज़र तो करते हो तुम मुझे।

        मुझसे यह अधिकार तो मत छीनो,
        नहीं बनना चाहती मैं अजनबी
        तुम्हारा होना मुझे एहसास दिलाता रहा है
        कि हम भी थे कभी साथ,

        बिल्कुल उन कहानियों की तरह,
        जो तुम्हे पढ़नी बहुत पसंद थी।
        बिल्कुल उन रास्तों की तरह,
        जिन पर तुम्हे चलना पसंद था।

        बिल्कुल उन पंक्तियों की तरह,
        जो तुम गुनगुनाया करते थे।
        अब तो सब नीरस सा हो चुका है,
        बस तुम्हारी यह नाराजगी ही तो प्रमाण है,

        हमारी उन प्यारी यादों का।
        इस अवसाद भरे मेरे जीवन का
        तुम ही तो प्रसन्न प्रज्वल दीप!
        नही सह पाऊंगी मैं तुम्हारा गैरों सा व्यवहार।

        बस इसीलिए सोच लिया है मैंने
        नहीं सुनना चाहती हूॅं मैं अब तुम्हारी कोई कहानी,
        और न ही समझाना चाहती हूॅं तुम्हे कुछ,
        ये जो है, जैसा है,
        बस वैसा ही छोड़ दूंगी मैं!

       




        """
        st.write (html_code,unsafe_allow_html=True)

    container = st.container(border=True, height=500)
    container.subheader("बनारस")
    container.divider()
    container.image("https://img.artpal.com/92108/23-16-11-7-8-1-17m.jpg")
    with st.expander("Click here to read"):
        html_code = """
        <h1 style='font-size:16px;'>
        तुम हमेशा रहे हो मेरी कहानियों में,
मेरे किस्सों में, और मेरे दिल में,
आज मैं तुम्हें अपनी कविता में भी उतारने जा रही हूं।

डर लग रहा है कि कहीं तुम्हारा ज़िक्र आते ही,
मेरे हृदय में जो अहलाद की भावना उत्पन्न होती है,
अगर उसे इस कविता मे नहीं उतार पाई तो?
अगर तुम्हारी सौम्यता और प्रेम को शब्दों में नहीं लिख पाई तो?
अगर तुम्हारे सौंदर्य के साथ नहीं कर पाई मैं न्याय फिर?

पर फिर भी आज मैं लिखूंगी
तुम्हारे सौम्यता, सौंदर्य और प्रेम पर नहीं,
तुम पर।
तुम्हारे उस गुण पर जिसके कारण सब तुम्हारे मुरीद हैं,
तुम्हारे अंदर के अपनत्व पर!

काशी की धरती पर उतर कर,
तुम्हारी हवाओं को अपने अंदर महसूस कर,
मेरे मन में सिर्फ एक ही ख्याल आता है कि
कैसा होगा वो बनारस जिस पर,
स्वयं महादेव ने कदम रखा था,
जिसे मां पार्वती ने अपनाया था?
और कैसे?
कैसे?
आज भी तुम उसी निस्वार्थ, निश्चल प्रेम के साथ सबको अपना रहे हो।

अभी बीएचयू के विश्वनाथ मंदिर में बैठ कर मैं सोचती हूं,
की आखिर कितने रंग हैं तुम्हारे?
तुम बाहर से जितने व्यस्त और व्याकुल नज़र आते हो,
अंदर से तुम उतने ही शांत और स्थिर हो,
मानो वो चिड़िया जो बार बार तुम्हारे पास आ रही है,
पूछ रही हो तुमसे, कि कैसे हो तुम इतने निश्चिंत और मौन?
वो जानना चाहती हो तुम्हारी हर एक कहानी,
पर तुमने अपनी प्यारी सी मुस्कान के साथ,
धारण की है एक चुप्पी,
जानते हो,
ये चुप्पी मझे चिन्तित या बेचैन नहीं करती,
बस भर देती है आह्लाद की भावना से,
क्यूं? मैं नहीं जानती,
या जानना ही नहीं चाहती।

अभी आधी रात को अस्सी घाट पर
एक नाव वाले की चौकी पर बैठ कर,
मैं सोच में पड़ चुकी हूं।
मनुष्य की अंतिम यात्रा तुम ही क्यों होते हो?
ऐसा कौन सा सुकून है तुम्हारे भीतर?
यहां लोग आभाव में भी खुश हैं?
उस फुग्गे बेच रही छोटी बच्ची के चेहरे पर देखी है,
 मैंने एक मुस्कान,
जो मझे याद दिला रही है,
पास बहती उस निर्मल धारा की।
मैं उसे लाचार नहीं समझती और न ही मुझे तरस आ रहा हैं उस पर,
मझे दया आ रही है खुद पर।
और मुझ जैसे हर उस इंसान पर,
जो कभी भी नहीं मुस्कुराया तुम्हारी तरह,
तुमसे नहीं छीन सकता कोई, तुम्हारी ये पवित्रता!
जिस तरह सबके पाप धोकर भी,
गंगा निर्मल और शालीन है।
मैंने देखा है उसमें तुम्हारा प्रतिबिम्ब,
बिलकुल स्पष्ट और विशद!

थक कर अब मैं दशाश्वमेध की सिद्धियों पर बैठ गई हूं,
मैं आज गंगा आरती देखनी आई थी,
पर उससे पहले मेरी नज़र टिक गई है,
उस विभाजन पर जो मै अभी देख रही हूं,
मेरी ही तरह कुछ लोग घाट पर बैठें हैं
और कुछ क्रूज पर बैठ कर
देख रहे हैं ये आरती,
कुछ बच्चे खेल रहे हैं ,
बैठ कर अपनी मां की गोद में,
और कुछ नीलकंठ का भेष धारण कर
देख रहे हैं उम्मीद भरी नजरों से उनकी ओर।

शायद तुम्हारी भी कुछ कहानियां होंगी,
जो मैंने आज से पहले नहीं सुनी,
शायद तुम भी चुप-चाप सह रहे हो वो पीड़ा।
इस क्षण में तुम मुझे महसूस हो रहे हो,
मानो बिलकुल उन घंटियों के स्वर की तरह
जो मेरे कर्ण से होकर,
मेरे हृदय में अनंत के लिए स्थपित हो गई हैं।
यहां बैठकर मेरे मन में कोई सवाल नहीं आया और ना ही आया कोई जवाब,
बस आज मैंने तुम्हारे देवत्व का संचार यहां की हवाओं में देखा है,
तुम्हारे मनुष्यत्व का भी एहसास हो चूका है मुझे,
अब नहीं हो रही मुझे कोई थकान,
पर मेरे अंदर इतनी हिम्मत भी नहीं,
कि यहां से उठ कर जा सकूं।

अभी वाराणसी स्टेशन पर बैठ कर,
मैं इंतजार कर रही हूं अपनी वापसी की ट्रेन का,
मझे तुमसे दूर जाने का आभास
अभी तक नहीं हुआ है।
मैं अब भी खोई हूं तुम्हारे उन मौन प्रश्नों में,
उन अनुत्तरित सवालों में।

मेरी ट्रेन अब मेरी आंखों के सामने आ कर खड़ी है,
बस अब इस क्षण में मेरा दिल मुझे तुमसे दूर नहीं जाने दे रहा है,
इस भिड़ में भी,
तुम मझे उसी विश्वनाथ मंदिर के,
छत की शांत संध्या की याद दिला रहे हो,
पुल पर गंगा को अपने सामने से गुज़रते देख,
भर आया है मेरा हृदय और मेरी आंखें,

अपने सवालों के जवाब ढूंढने आई थी,
अपनी जिंदगी का एक अहम हिस्सा तुम्हारे पास छोड़ कर जा रही हूं,
तुमसे सीख कर जा रही हूं,
निश्चल मुस्कुराहट की अदा,
तुम्हारी सौम्यता और सुन्दरता,
जो तुमने काशी की गलियों में बिकेरी है,
उसे अपने अंदर समेट कर,
मैं ले जा रही हूं अपने साथ।
भगवान विष्णु की तपस्या
और महादेव का आशीर्वाद,
सब महसूस किया है मैंने,
तुम्हारे हर रस की अनुभूति जा रही है मेरे साथ,
छोड़ कर जा रही हूं,
अपनी सारी चिंताएं बाबा विश्वनाथ के चरणो में,
और ले जा री हूं अपने साथ
खुद को।

बनारस मैं जा रही हूं,
तुम्हे,
अपने साथ ले कर,
मैं जा रही हूं।

       




        """
        st.write (html_code,unsafe_allow_html=True)
    

    container = st.container(border=True, height=500)
    container.subheader("Enchanting Dream")
    container.divider()
    container.image("https://reformjudaism.org/sites/default/files/hand%20holding%20heart.jpg")
    with st.expander("Click here to read"):
        html_code = """
        <h1 style='font-size:16px;'>
       I froze at that moment,
no heed to the scorching heat,
one look into your eyes,
I was up for a long ride intact on my seat.

I giggled, reading your text over and over.
My heart raced every time you messaged me first.
Your beautiful face and enthralling smile
were like a breath of fresh air on a hot day, quenching my thirst.

Sneaking glances at you and then glancing away,
Smiling in bed, remembering every conversation of ours.
Your every word was like a soothing cure to my wounded soul,
Listening to your melodious voice, I spent hours.

You were like the leaves of Gulmohar,
Adoring the picturesque tree took my breath away,
And even when you fall,
You mark everything red, making me fall for the enticing pathway.

How I wanted to spend each moment with you,
holding you in my arms tight while calling you by my name.
Just then, the spell broke; I opened my eyes only to realise,
"You" were an enchanting dream.
       




        """
        st.write (html_code,unsafe_allow_html=True)

















# Sidebar navigation
st.sidebar.title("Dive Into My Creations")
page = st.sidebar.radio("Go To", ['Main Page', 'Book Reviews','My Writings'])

# Display the selected page content
if page == 'Main Page':
    main_page()
elif page == 'Book Reviews':
    book_reviews()
elif page == 'My Writings':
    my_writings()    


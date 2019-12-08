close all

try
    python_version = pyversion;
    fprintf(2,'** Python Version : %s\n',python_version);
catch e
    fprintf(2,'** Error : %s\n',e.message);
end

% Import art lib (version > 4.2)
artlib = py.importlib.import_module('art');

% text2art function
% text2art(text, font=DEFAULT_FONT, chr_ignore=True)
art1 = artlib.text2art('art1');
disp(char(art1));

art2 = artlib.text2art('art2','block');
disp(char(art2));

art3 = artlib.text2art('art3','white_bubble');
disp(char(art3));

art4 = artlib.text2art('art4','random');
disp(char(art4));

art5 = artlib.text2art('art5','rand-small');
disp(char(art5));

art6 = artlib.text2art('art6','rand-medium');
disp(char(art6));

art7 = artlib.text2art('art7','rand-large');
disp(char(art7));

art8 = artlib.text2art('art8','rand-xlarge');
disp(char(art8));

art9 = artlib.text2art('art9','wizard');
disp(char(art9));

art10 = artlib.text2art('art10','random-na');
disp(char(art10));

art11 = artlib.text2art('art11','mix');
disp(char(art11));

% tprint function
% tprint(text, font=DEFAULT_FONT, chr_ignore=True)
artlib.tprint('art12');

artlib.tprint('art13','block');

artlib.tprint('art14','white_bubble');

artlib.tprint('art15','random');

artlib.tprint('art16','rand-small');

artlib.tprint('art17','rand-medium');

artlib.tprint('art18','rand-large');

artlib.tprint('art19','rand-xlarge');

artlib.tprint('art20','wizard');

artlib.tprint('art21','random-na');

artlib.tprint('art22','mix');

% tsave function
% tsave(text,font=DEFAULT_FONT,filename="art",chr_ignore=True,print_status=True,overwrite=False)
response = artlib.tsave('art','standard','test.txt');
disp('art1 message :')
disp(char(response{'Message'}))

response2 = artlib.tsave('art2','block','art.txt',true,false);
disp('art2 message :')
disp(char(response2{'Message'}))

response3 = artlib.tsave('art3','block','art.txt',true,true,true);
disp('art3 message :')
disp(char(response3{'Message'}))
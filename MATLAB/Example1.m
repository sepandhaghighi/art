close all

try
    python_version = pyversion;
    fprintf(2,'** Python Version : %s\n',python_version);
catch e
    fprintf(2,'** Error : %s\n',e.message);
end

% Import art lib
artlib = py.importlib.import_module('art');

% text2art function
% text2art(text, font=DEFAULT_FONT, chr_ignore=True, decoration=None)
% Note : There is no need to use 'chr_ignore' flag in MATLAB 
% unsupported characters will be displayed by a question mark ('?')
art1 = artlib.text2art('art1');
disp(char(art1));

art2 = artlib.text2art('art2','block');
disp(char(art2));

art3 = artlib.text2art('art3?','block');
disp(char(art3));

art4 = artlib.text2art('art4','white_bubble');
disp(char(art4));

art5 = artlib.text2art('art5','random');
disp(char(art5));

art6 = artlib.text2art('art6','rand-small');
disp(char(art6));

art7 = artlib.text2art('art7','rand-medium');
disp(char(art7));

art8 = artlib.text2art('art8','rand-large');
disp(char(art8));

art9 = artlib.text2art('art9','rand-xlarge');
disp(char(art9));

art10 = artlib.text2art('art10','wizard');
disp(char(art10));

art11 = artlib.text2art('art11','random-na');
disp(char(art11));

art12 = artlib.text2art('art12','mix');
disp(char(art12));

artdecor = artlib.text2art('art decoration','white_bubble',true,'chess1');
disp(char(artdecor));

% tprint function
% tprint(text, font=DEFAULT_FONT, chr_ignore=True, decoration=None)
% Note : There is no need to use 'chr_ignore' flag in MATLAB 
% unsupported characters (out of 95 printable characters) will be displayed by a question mark ('?')
artlib.tprint('art13');

artlib.tprint('art14','block');

artlib.tprint('art15?','block');

artlib.tprint('art16','white_bubble');

artlib.tprint('art17','random');

artlib.tprint('art18','rand-small');

artlib.tprint('art19','rand-medium');

artlib.tprint('art20','rand-large');

artlib.tprint('art21','rand-xlarge');

artlib.tprint('art22','wizard');

artlib.tprint('art23','random-na');

artlib.tprint('art24','mix');

artlib.tprint('art decoration','white_bubble',true,'chess1');

% tsave function
% tsave(text,font=DEFAULT_FONT,filename="art",chr_ignore=True,print_status=True,overwrite=False,decoration=None)
% Note : There is no need to use 'chr_ignore' flag in MATLAB 
% unsupported characters (out of 95 printable characters) will be displayed by a question mark ('?')
response = artlib.tsave('art','standard','test.txt');
disp('art1 message :')
disp(char(response{'Message'}))

response2 = artlib.tsave('art2','block','art.txt',true,false);
disp('art2 message :')
disp(char(response2{'Message'}))

response3 = artlib.tsave('art3','block','art.txt',true,true,true);
disp('art3 message :')
disp(char(response3{'Message'}))

response4 = artlib.tsave('art decoration','white_bubble','art.txt',true,true,true,'chess1');
disp('art4 message :')
disp(char(response4{'Message'}))

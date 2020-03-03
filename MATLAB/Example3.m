close all

try
    python_version = pyversion;
    fprintf(2,'** Python Version : %s\n',python_version);
catch e
    fprintf(2,'** Error : %s\n',e.message);
end

% Import art lib
artlib = py.importlib.import_module('art');

% decor function
% decor(decoration, reverse=False)
% unsupported characters will be displayed by a question mark ('?')
decor1 = artlib.decor('barcode1');
disp(char(decor1));

decor2= artlib.decor('barcode1',true);
disp(char(decor2));

decor3= artlib.decor('chess1',true);
disp(char(decor3)); 

art1 = decor1 + 'art test' + decor2;
disp(char(art1));

art2 = decor1 + artlib.text2art('art test','white_bubble') + decor2;
disp(char(art2));

art3 = decor1 + artlib.text2art('art test','white_bubble') + decor3;
disp(char(art3));

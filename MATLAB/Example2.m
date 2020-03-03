close all

try
    python_version = pyversion;
    fprintf(2,'** Python Version : %s\n',python_version);
catch e
    fprintf(2,'** Error : %s\n',e.message);
end

% Import art lib
artlib = py.importlib.import_module('art');

% art function
% art(artname, number=1, text="")
art1 = artlib.art('coffee');
disp(char(art1));

art2 = artlib.art('love_you',int32(1),'test');
disp(char(art2));

art3 = artlib.art('random');
disp(char(art3));

art4 = artlib.art('rand');
disp(char(art4));

% aprint function
% aprint(artname, number=1, text="")
artlib.aprint('coffee');

artlib.aprint('love_you',int32(1),'test');

artlib.aprint('random');

artlib.aprint('rand');

% randart function
% randart()
artlib.randart();

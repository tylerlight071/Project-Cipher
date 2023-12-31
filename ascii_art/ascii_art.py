# ASCII art to be displayed
cipher_art = """
@@@@@@@@@@@@@@@@@@@#&@.*,&&(  &&@&&.*(//,,,,&&&@@&%&&&&&/&&&&&&@@&@@@@@@@@@@@@@@
@&&&@&&&@@@&&&&@((&##,/#/&   &&@.../*,,,,*//***///***/%&&%((&&&&@@@&&@@@@@@@@@@@
@&&&&&&&@&@@@&&&(((((&.,,,,  &( ,..,,,,,,,,*/**,.....,/&&&&&&&&&/*/&@&&&&&&@&@@@
@&&@@@@@&&&&&&&&((((%*, . ..   ..........,,,*,,,,,,/(////**////****#@@&&&@&&&&&&
&&&&&&&&%#&&%#(//,         ..   .,.....,.,,,,,,,,/////****,,,,,,%&&&&&&&&&&&&&&@
@&&&#@&&&&%####((/               ..,....,.,,,,,*///////**,,,**,,&&&&&@&(((&&&&@@
@&&@@&&@&@&&###*.                 . *, ...*,.,,*//,**,,,,,,,.*/(((((((@&&@@@@@@@
@@&(&&&#&&&%&..        .     ./###%%#(.    ...,,,,,,*** ..,.    ,#(#&&&&&&@@@@@@
&@@((((((&//. .*.         .*,(#%%%%%%&%%%%%%%%%%%%%%%%%#(..  .& .,@@&&&&&@@@@@@@
@&&(((((((((((/           (((*((%%%&&&&&&&&&&&&%%%%%%&%%#(..  .@#*&*@&&&&@@@@@@@
@@&(((((((((((..   .    .//(######%%%&&&&&&&&%%%%%%%%&%%%(,,..,.&/@&@&&@&@@&@@@@
&&&&((((((((((. / . , ..///(######%%%%%%&&%%%%%%%%&%%%&&##. ..%.&&&&@@&&&@@&@@@@
&&&&((((((((((./.    . /((((((((##%%%%%%%%%%%%%%%%%&%#%%%#(  .&(&&&&@&&&&&&&@@&&
&&&&&&(((((((**//      (((/..*,.    .#%%%%%%%%%%%###(*..*((..&&&&&*&&&&&&@@%%%&&
&&@&&&&((((/**((,.#   ,(((####%(/(,,,,,(%%%%%%(.   *((####..&&&&@&@&&&&@@%%%%&&@
&&&&&&#/(((((((%##,.. ,((##%#,*%, ,%%*%((%%&#((*.. ,&..#%%.&&&&@%%%%&&@%%%%&&&@@
&&&&&(///((((((&#%,., ,((#%%%%######&%%%##%&#%%&%%(//#%%%#&&&&&&%%%%%%%%%%&&&&@@
@&@#&&&&((((((((&%%&,* /((#%%%%%%%%%%&&%#%%%%%%%%&%%%%%%#*&@@@@%%%%%%%%%%&&@@@@@
&@@@&&&&%%&%((((((%&&(/*//(#%%%%%%%&%%%##%%%%#%%%%%%%%%(&&&&&@&%%%%%%%%%&&&&&@@@
&&@@@@&&&&&&&&&((((((/ *////(%%%%&&&&&/((##&%%(%%%%%%%#%@&&&&&%%%%%%%%%&&&&&&&@@
@&&&@@@&&%&&&%&&&&&&##  *////(%%%%%&&&%/*****/%%%%%%###&&&&&&&&&%%%%%%&&&@&&@@@@
@&&&&@@@&&%&&&&&&&&&&&  .**////#%%%%%%%%%%%#%%%%%%%%#%&&@%%%%%%%&&&&&&&&&&&&@@@@
@&&&@@@@%%&&&&&&&&&&&#&.,.***//#%%%,,**..,/.,,.*%%##&&&&@%%%%%%&&&&&&@@@@&&&@@@@
@&&&@@@&&&%/((&&&&&&&&(**,..,**//%%%%##(((####%%%#&&&&&&@%%&&@&&&&&@&@@@&&%&&@@@
&&&&&&&&&&&//(&&@&&&, ,*//,...,***/#%%%%%%%%%%%%&&@&&&@@@&&&&&&&&@@@@@%%%%&%&&@@
&&@&&&&@@@&//(&&&&... .//(#(,,,,,.,*(#%%%%%%%%#,.(&&&(&&&&&&@@&&&@@@@@&%%%%&&&&@
&&&&&@&&&@@@/(&&&...   ./###%#,,,,,..   ....,//    ./&&&&#&&&&&@&@@&@&@@@&%&&@@@
@&&&&&@&&@@@&#&,....    .###%%%#**,,,,.,,***/**      .#*&&&@&&&@&&@@@&&@@&&&&@@@
@&&&&&&&&@@@%.,,,,,,, ..  #%%%%%%#******%#(///,    .,,,/&&&&&&&@@@&&@&&&&&&&&&@@
&&&&&@&&&/. ..  ..,,.,.    (%%%%%%%%%###%###/./. ..,.,(*((&&&&&&&&@@@@@&@&@@&&@@
@&&&   ..   .. .  .,,,,,      #%%%%%%%%######//,  .,...#.,     *&&@&&&&&&@&@@@@@
 .  .,        ... ...,,,,.         #%%%%%###(     ... * .          ((/&&@&&&&@@@
"""

sender_art = """
.....,,,,,,,,,,,,,,*@@.,,.   ..    . . .                      ..%,,,,,,,,,,..,..
...,,,,,,,,,,,,,,*&@@%..  ..      ....                   .      .,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,**/@@,,,, ..       ......                          ..,,,,,,,,,,,,,
,,,,,,,,,,,,***/@@/*,..*..         .....                          ..,,,,,,,,,,,,
,,,,,,,,,,,**//@@@*,.,/#(...       . .....                         ..**,,,,,,,,,
,,,,,,,,,***/(@@@@#**%%%##,..        ......... .  ......,.          .,*,,,,,,,,,
,,,,,,,****//@@@@@@###%&#/,..             ........,((((////*,       ..,/*,,,,,,,
,,,,,,****//#@@@@@/*#/*##(,.                .....(#((((((///*,       .,//*,,,,,,
,,,*******/(@@@@#((*,,*(((,..                ../##(((((((///**  .  ...,*//******
*********//%@@@@/#%%(/*,/.,.               ..,####(((((((((//*,. . ...,*********
*********/(&@@@*,**,.,*/,.,.            .../%%%####(((((((((//*. ...,.,,********
********//%@@&((.,...../,.          .,***,...../((((((((((((/,,,,...,,,,********
********#%&@@&/,,*/,.,...... ...,,.... .  . .....,*//(((/*,,,,*/( ..,,*,///*****
*******###&@@&/,./(*......,,,,*/////*,*#%%%%(.,,,*/((##**.//(( ..  ..,*/////****
******(((%&@@%*,..(*//,.*,*/%(//((####(((/////(##((##%((//////#/   ..,*/////////
*****(((##&@@#*,..../(//***/@&(//((##%%######%####(##(##((((((((   ..,/*(#######
**/////(##&@&#*,...../%%%**/#@&(*//(((#########(((((((%&%##(##%#.  ..,*((#%%%%%%
//////(((%@@&#,,.........  /#@@%/**///(((((((((////(###%#####%%.   ..,/*/(%%%%%%
/////(/((&@@%#,,......     .@%%%#/**///((((((##,,...,,*%(##%&&.  . ..//(((#%%%%%
///////#%&@@%#,...... .     @@%#((/**///(((#######(/*/(##%&&%   . ...*(/#((%%%%%
//////(#%&@@%#*...... .     .@&%((//////////(((/*,,**/%&&&&#   .....,*/(##/#%%%%
((((((((%@@@%(*...... .     .,,@&#(//**///(((((((/***/%%%&,  ......,*(((##(#%%%%
########&@@@%/*.....        ..,,,,&%(/**///////*,,,/%%&&%.  .....,///#######%%%%
&&&&&&&@@@@@%/,.....   .    ..,,,,....#////((##%##(##&&. ...,.,/((((#####%#%%%%%
@@@@@@@@@@@@%/,,.....      ...,*,,*,..... **///////#&.......,((/((##%%%%%%%%%@@@
@@@@@@@@@@@&%*,......      .. .******,...... .    .. . ... .   .....,#%%%%%%@@@@
@@@@@@@@@@@&#**......          ,*******,.....              .....,,,,***,,,/%&&@&
&@@@@@@@@@@&#**.....           .,********,.              .....,,,.,***,**,#/////
&@@@@@@@@@@&#*,.....            ,*.. .                  ...........,.,,,,,,,,,,*
&@@@@@@@@@@%(,,....             .*.                    ..........,...,,***,,,,.,
&@@@@@@@@@&%/,.....           .,,, .                  .....,..,,,,,,,,,*/((/,,..
&@@@@@@&%%#(,.....           .,,*, *              .. .....,.,(&&&%*,,,,,,*/. ...        
"""

camera_1 = """,,,,,,,,/,,,,,,,,,,,,,,,/,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,*****************,******
,,,,,,,,,*/,,,,,,,******,,/,,,,,,,,,,,,,,,,,,,,,,,*,**********************,,,,,,,,,,,,,,,,,,,,******************/*******
,,****,,,,,,/*************,*,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,/**********************/***
**********,,,*/**************,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,*,,**,****,,,,*/***************************
****************/************/,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,***,*******,*********/////**********************/**
******************/*********************************************************************/////////*//**////*****/********
///(///////////////(//(((((((((((******////////////////////////////////////////////////(#############(#(((((((((((((((((
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,**,,****,,,,,,,,,,,,,,,,,,,,,,,,*,,,***,***
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,****,*,*,,,,,,,*,**************************,,,,*****,*,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
********************,**,,,,,*,,,,,,,,,,,,,,,,,,,,,,,,,,,*,,,,,,,,,,,,,,,,,,,********************************************
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,...,,***,,,,,,,*,,,,,,,,,,,,,,***************
(((############%%%%%%%%%%#,,,,.. *.  ..,,,,,,,,,,,,,,,,,,*,,,,,,,,,........... ,,,,,,,,,,,,,,,,,,,,,,,,,,(**************
///////////////(//((((///#,,,,.. . ,.  ...,,,,,,,,,,,,,,,,,,,,,,............   ,,,,,,,,,,,,,,,,,,,,,,,,,,(***/****,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,,#,,,,...... ..  ....,,,,,,,,,,,,,*,,,.............    ,,,,,,,,,,,,,,,,,,,,,,,,,,* **.          
              ......,,,,.#,,,,,........ *  ....,,,,,,,,,,,,..............      .,,,,,,,,,,,,,,,,,,,,,,,,,/,/,/,,,,,,,,,,
.,,,,,,,,,,.,,...,.,,,...(,,,,,,,,,...... ,  .........,,,,,*.,,..........      .,,,,,,,,,,,,,,,,,,,,,,,,,/,/,/,,,,,,,,,,
 . ............,.,,,.,.,,(,,,,,,*,,,.,,...  .  .......................         .,,,,,,,,.,.,,,,,,,,,,,,,,//*/*///(/////(
,,.............,,,,,,,,,,(,,,,,,*,,.,*,,......   ...,,,,,,,,,,,.......         .,,,,,,,..........,,,,,,.,//*/*////(/////
.....     ...........,...(,,,,*,**,,,**,,.,.,...*************///////////       .,,,,...................../(*/*((///*****
 .......     ............(,,,,**,**,,**,,,,,,,,.//********//////////////       .,,......................./,,/*////****..
 .......      ...........(,,,,**,,***/*,,,,,,,,,*****************//*///*       .,,......................./,,****,/****,,
 .......       ..........(,,,,,*,****//*,,,,**,*/////////////(((((((((//      ,.,........................*,*,/****/*//,,
 .......       ..........(,,,,,*,****/(**,,******,,,,(***,,,*..  ..,.... .  .............................*.,,*...,,,**,,
..........   ............(,,,,*,,((**/(**,******...../,,,...,,,.,*,,,,*(..../*...........................*,*,/*,,,,,**,,
.........................(,,,,/*,(/*,(/*******/*...../.,...,,*,,,/,....,,.....,..........................****/*,,,,,**,,
........................./,,,,/,*//*,/(****,**/*.....*.,,,.,,/*,,(#....,,,...,,..........................****//*******,,
............,/#*,.......,/,,,,*/*****(/*******/*&,..&&%*,.(,,/*,,(((#,,*,,,,*/,..........................***(/********,,
,,,,.,,,...,.///,,,,,,.,,/.,,,/,////*(/***/,**(/#(..%%%&%%&*,/**/@%#..(#,,,,,,,..........................****/*%%&(***,,
////,,,,,,,,#((/,,,,,,,,,/.,,,*/*//**#(***//*//*&&#/##%%#((*,//,,@@#/*%%*,,,,,,..........................***,//&&//*,,,,
//*/,,,,,,/(#(*(((.,/#%*,/,,,,//,//**((***,,/////%(//(&#%%(/((/(%&##*###*,,,*,*..........................*//**(#/(#(,#,*
####....,*/(//(&&#((((*,,/,,,,////(**((**,**//((%@&,(/#((##(((((((######*,,,,**..........................*//(/(&%**@%#(*
(*(##%%&@&%&&(&%&#(((%***/,,,,///,#**(#///(////*&@%*###((####((((//((((#*,,,,,*..........................*(/(/(#&(*,&&#(
&&&,&%%,,*%,%(%&%###(#%**/,,,,//((#*(##*/*//*//*(///*(((((#(##(/(###%###*,,*,,*..........................*#/#/%%%&%%%#(*
&***(%@&&(/&&#(&&/(#%/***(,,,,/(*/#/((#//*(//**(#########%%%%%%%%######%%*,,*/*..........................*#/#(%%%/@@&&@@
&%%%&#@#%%%(@#%#%/%&%%%%%/,,,,/(((#/*##//,/,,#(((((((((####%%%%%%########%%%**(..........................*%*#(%%%@&@&&&@
&&@#%&%&%&@&&%&#&&%%%%%%%/,,,,((#(#(/##/*,*#((((((((((#########%%####%#%%%%%%**..........................**/*(***/%(%@@%
////**,*,*,/#*%@%((,%&%%%/,,,,(((/#*##,,((((((((((((((##################%%%%%&*..........................(&/%%&&&&&@@@@@
......,,,@@#&@@@@@@%&%%%%/,,,,(#(/((,,#(#####(((#(##############%#######%%%%%%%..........................(&*#%@@@@@@@@&@
..,,*((%&&&&&&&&&&&&&%%%%(,,,,(((,,,(####(((((#(((###############&&%%&&&&&&&&&%,.........................#&/(%&@@&...   
*((((&&&&&&%%%%%%%%%%%%%%/,,,,(,,*(####(###(##(##################%%%&&&&&&&&&&&,,,,,.............,....,.,#&(*%&&&&&%&,..
(#####(##((((((/###(#####/,,,,,#####((#(#(##((#(#########################%%%%%%,,,,,,,,,,,,,,,,,,,,,,,,,,/((/((////((((*
((&%%%%%%%%%%%%%%%%%%%%%%%%%%##########################%%%%%#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%&%&&#@&&&&&&&&&&&&&
((%%%%%%%%%%%%%%%%%%%%%%%%############################%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%&&&&&&&&&&&&&
(((%%%%%%%%%####%%%%%#%#((((((/(//((((((/(((((((((##((######%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%&%%%%%%%%%%%%%%%%%%&&&&&&&&&&
(((#######%%#%###%%%#(((/((((/((((((/(((((#(##(((####(((((########%%%######%##%%%%%%%%%%%%%%%#%%%%%%%####%%%%%#####%%%%%
(((%%%##(#%%%%%%%#((#((#((####(#####(##((#(######((######(((#(#################%%%%%%%%#%%%%%%%%%%%%%%%%%%%#########%%%%
(((%%%#%%##%%######(((#(/((((#(/(#####((#######(##((#%#####%##################%%#%%#####%%%%%%%%%%%%%%%%%%%%%%%%%%#%%%%%
(((%%%%%%%%##%((###(#/(##((((((##((##(##(##((##(#(((#(########%####%#%###%#%%%%%%%#%%%%%%%%%%%%%%%%%%%#%%%%%%%%%%%%%%%%%
(#(%#%#%#%(##(#(##(##(#((#((#####(##(#########################(###%%##%%%%%%%%%%#######%%%%%%%%%%#####%%%%%%%%#%#%%%%%%%"""

camera_2 = """##(((//,///***(%#(%%%%%%%%%%%%%%%%%%%%%%%&&&&&&&&&%%#%%&&&&&&&&&&&%#%%%%%((((((%/.(#%%%%%%%%%%%%%%%#&%##%%&&&&&&&&&&&%&&&&&&&&&&&&&&&%%&&&&%%%%%%%#%%%%%%%%#####################((((
@@@@&&%/#%&@@@@##########(/(#%&&&&&&&%%%&&%&&%%%&&&&&&&&&&&&&&&&&%%%%%%%%%%%%%%%%%%###(##(//(#(/&&%%&&&&&&&&&&&&&@@@&&&&&&&&&&%%%%&&&&&&&%%%%%%%%%%%%%################(((//(((((((((
@@@@@@@#@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%##(#%&&&&%%%%&&&%%%%%%%%%##%%%%%%%%%%%%%%%%%%%%&&&&@&&#((((#(#%%&&&&&&&&&&&%&@@%%%%%%%%%#%########%%%############(####((((((((((((((
@@@@@&&#&&@@@@@%%%%%%%&&&&&&&&&&&&&&&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%##((#%%%%%%#(/#%%%%%#%%%%%%&&%%%%%%%%%%%%%#/(((///((,(#########%%@&%######%########(((((((((((((((((((((((///
@&&&&&&(&&&@@@@%&%%%%&&&&&&(*&@@@@@@@@@@@@@@//@@@@&&%%%%&&&&&&&&%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#(##%##(%%&&&%%%%%%#%%%%##(((######(///**/*,(####(/**/((((//////(//*////////**,*******
&&&&%%%/%%&&&&&%%%%%%&%&&&&/*&@@@@@@@@@@@@@@((@@@@@@@@@@@@@(@@@@@@@@@@(/@@@@@@@@/,@@@@&%##%&&&&&%@@@@@%%%####((((((((((/**/(((#((((//**/((((((##@@@@@@%%##(((((((/(((((/(//***@*****
##%%%%%/%%%%%%%*/,*///(@@@@/*&@@@@@@@@@@@@@@((@@@@@@@@@@@@@(@@@@@@@@@@(/@@@@@@@@(,&&%&%&(/,####&@@@@@@,.((*,. ,..  ,*//((/((((((((%(####&%&(#%@@@@@@@@@@&%%#(((((*(((((/(////*******
(#####%%######%*/,,**#&%%&&/*&@@@@@@@@@@@@@@//@@@@@@@@@@@@@(@@@@@@@@@@(/@@@@@@@@/,&&&%##(*,##%&@@@@&&&*.(##(/.(*(  //* #(,,##(##%%%(,%%#(%(%&@@@@&&&&@&@@@&&%##((/(((((/((///*,*,* /
((((##########%//*//((//#%%*,&&&@@@%&@@@@@@&//@@@@@@@@@@@@@/@@@@@@@@@@/*@@@@@@@@*.%%%%%%(**%&&@@@@%%%%,.((((# #*,.,#/##,#((##%#####(###/(#/&&/&&&%&%(*%******%%#./*((((/((//**(*((,*
(((((##########,*,,,***&&&&*.##&&&%&&%&%%%%#**&%&&%%%&%%%%%*#%%%&%&&@&**/&%%###%,.&((/(&(*/%&&&&@&%%(%,.((,.,#@@@@&##,#*,**(,##*((,*(/**##.%&&&/(%*/*,(#/#(/%*%*%( , /((#(//**//**,/
((((((#########,../,,*,%#%#,,(%#%#%&##%%%((#,,%%##%##%%%%%#*(*#,&(&##&*,##%//(%#, #(*,,,,,#%%%%%&&#,***,(#.   .#,,,,. .  ..,,,.... %(..*/*(/***(**#/,/#(,(*#/(,.,.**.,####//** /   /
/((((((*####((#/,//*(%%##(/,./(###%%###%**//&%#(#%////,*%##*#,&&&&&&&&*,/,&%%**,,.#(,,,,,,,###&####**,**,,,*%%%%%%%%%##,..,,*//*,,*%%%%(%#%#.../.,/*,.#%%%#*########((/#%#(/**(*#(#%
/(((((((#####(#///##%%%%%%(.,..........***#*%%%%%%*/*,,,@%%%&&@@@&************#&&&&&&&&&&&&&(*, **.####(*,,,%%&&&%%%%##,,,,,*/*,,..,#%%%%&%%./(**,/,,,*,*(#%%%%%%%%%%(%#%#((****////
/((((((((####(#......,,(#(# .*##%%(/*/%/(##%#(((#%(,,,/(&%%%&&%%%%,,,,,,,***,*/*&@&&&&&&&&&&(./.##/@&%(*,@@&&@&##*./**.,.#####((#####&&&%%%%.../*..,,..,*(#%%%%%%%%(((%%%#/(*******/
(/((((((((((((#//....,*%//%, ./@@@....*/@@@%%&&@&&##%%%(@##%%%%%%%,,,,,,,,,,,,**%%%%%%%&%%%%%###,,,*(**,..,,,,(/(./( ((((##(/(/(#&&&%%%#@&@@@&&%***(%###/##%%%%%%%%(((%#%(//**.,*,,*
//(((((((((((((%%(**%(/**##(..  ** ...*@@@&&&#(((%# .#%&&%/(###%%%,,,,,,,,,,,*&#%%%%%%%%%%%%%%%#**** ,###/.#.(((*.   ...   ......,* (#%%%%%%%%%%/(#########%%%%%%%%(((###(/,,,,,,,,,
///(((((((((((#/////*(***//,//***, . . .*%&&&@@@@@&(...,,&@(#((%@&&%((%#%%(*//%%###%%%%%%%%%%%%%**.///##,/,&%%%%/**/,       ,#%#(/////%%%%%%%%%%/##(,#%#/##%%%%%%%%#(((##((/((/////*
////(((*(((((/#/*.  ,,... ./#,     /, .  *#*/ #@&@&%,  .,,&&&&&&&&&&%%%&&&&(%(((((####&&(##%%%%#@@@@&@&****%@@@&&&&#/  ..,  */#.**%###%%%%%%%%%%(%%#%##%###//////#%,,**//*//*//////*
//////(*(((((/(   ..../#((###%##%&%*%/.**.        /*,  ..,%&&&&&%/*(,*/,(%@&@@&&&&&&%%(((((###%#@@@@@@@@@@@@@@@@@@&&&&&&%#*//**,,** ((&%%%&&&&&&#%%#%%%%%%######((#####(#(//((/*/(((
//////(/((((//(%#%###(##((((.. ,.(*# */. .. /   ****,     .&&&&&&&&&&&&&*/&&@@@@@@@@%&@@@@@@@@@@@@@@@@@@@@@@@@@@&#((%%%%%%%**,,,,,,,,*%%%%&&&&&&#%%%%%%#%#######%%%###%####(/((/*/((
*////////(((//(#%%%%%%###  #(((.( //(((.((.////****/.     .//**#%&&&&&&&@@@@@@@@@@@@@&##@@@@@@@@@@@@@@@@&#%*%%%%%%%%%%%%%%%/.,,,,,,*,*%%%%%&&&&&########,,,//(((#(##(#((###/((/(/((/
*(/////(/(((((####%%#%## (#%%##(/((((((#,      ,,,,,      ,         .#&&&#%(#&@@@@((#%%%(%#@@@@@@##/#%%%%%%%%%%%%%%%%*%%%%%((((#(//(*//%%%%%%&&&####(,***//*//((///(/(((//*//(((((((
***/*//(/(((###%%%%%%%%%%%%%##%&%%#(   //(,(/  ..,*.*,*,.*.             .#######%###@@@@@##(/%%%%%#%%%%%%%%%%%%%%%%,,*#%%%%#(((#(%%%%###%(###/,((,**//(*///////////**////*//((/(/(((
##(######/#%%#%&&&&&&%%%%#####%#%.(#%##(*(*,*****/# */**,/*,         *//*############/##########%%##%%%%%%%%%%%%%%%#%%%%%%#%&%&%&%%%##%%%&%#(##%%%#####(*/(((((((//(////*/((/*/((*/(
#(((##(##*####%&%%%%&&&&%%%%%%%%..%#(#%##/ *(/*//,**#,.  (   ***  . ,. ..############/############(*,#%%%%%%%%%%%%%%%#%%%%%%%%%%%#%%&%%&&%%#&%#%#%%#((########((#((((((/((((/((((#(/
//(/#%#%#(/%##&&&&&&&&%&%##%%##%#%%%%&%#(#%#/(/((((((#//*     ,,,.*,,,*,,######%##%##/##########( (**#%%%%%%%%%%#%%%%%%%%%%%&&&%%%&&%%%&&%&%%##%%#/#%%%##((###((##(((//((((#(###((((
(#(#%%#%#%#(&(%%%&&%&&&&&&%%&&%#####(##(%%(####(###(/((*/*.     ..,*///*,######%%%%%%(##########(#(#%#%%%%%#%%%%%%%%%%%%%%%%#%%&###%%%&&%%#%%%#%#%%%%###%%##%#####(((##(##(####(((((
((/(((/(((((#%#%&%&&%&%%&#%%####((/((((##(##(((/*/**//          .,  .,,.,#####%%%%%%%(################(#%%%%%%%%%%%%%%%%%%%%%%%%#%&&&&%%##%%###%%%%%#%#%%%%%##((#(((###((((##(((#(((
*////###%(#%/#%%%%&%(##%%%#%#######(/(/((((#(((((/   /(///  .,,,,*   *,,,#####%%%%%%%(##########%/(###%%%%%%%%%%%%%%%%%%%%%%%%&%%%&%%##%%%%%%#%%%%%%%%%%%%############(((((((((((((/
(##(##%%%%&%%%%%#%%%%%%%###((/(#/(((#(#((((#((/ /((*,,,,* * . .,...., .,,####%%%%%%%%(######/#####(######%%%%%%%#######.,,/(##%%%%(#%%%%%%#%%##%%%%%%%###(##((((#((((((////((((((((/
#%(%######(((%%%%(&##(((#((/#(#(/#####((##(#(/   ,****,* */*** .*,*,  ..,####%%%%%%%%(#*##########(################,.*////////(((########%%%%###%%%####((####((((###((/(((((((//(///
#(((/#(/(###(//((##(####((/((##((#######/(//##(##(//(/,  *,* ,///**,***,*###%%%%%%%%%(#########################( .*////////**/((((((((######(%%#(((#%#############(##(((((((/(//////
#(*/*/*//////*/((#/(((((%#(/#((##(#(/((#(####(*##(((*(.  .//*,***,*///***%%%%%%%%%%%%#######################.,,*////*//////(///(//(((((((/#(##(((((((###(((#%###(#(((##(/((/(///////
%#/*,***//(/(///(/(/(###(#//((//((((##((((#(####((#%(/(((#//(///((/((/*,*%%%%%%%%%%%%#############(#####...**/////**//*//////////((((((#(((((//((/((((((##%%##((#(((##(//////*//////
#,*(//(((/((//*(##%%#((//(###/(((#((((#(((#(///(#(//****(//*###(*#(****//*,#%%%%%%%%%#############((*..,***////**////(/////**///((/(((((((///((/(((//(####%##(((((((((/////,////////
**(/*(**/####/#((##((((((/#(##(#(/(/(((#/(#(#(/*(////*****#/#((//****//*(*/**,%%%%%%%###########/ .,***////*,/////////////*//(///((((((/////(/////*/(########((#((((((//////////////
,,(((#(//(//(*(/(((////(#((/((/#(((%(//(/*((((///////***/(////(**//(/*/*(*((//**.##%%(####(#/ ..**********/////////////*//////(((((/////(//*////*//####((###(((((((***//////////////
/,//,**/*(***//**//((((/(###/#(%(#(*//*/(/(//(((/(//*((((((((##*##(#(((((#((////**,.%(##(..,,*******,*////////*/////***////(((/(/*/////(/((//////(#%#((###(*(#(((/**/////((/(///////
,*,,,**///***##/*/(/*(#(##((#(//((*#/////((((//(((/#(#*(/#(((*(#(###((/#(*(((((((*(**,.,.,******,,*//*/////*//////,*//////((//*//////////(((///(####(####((##((((///*///((//((///***
(*,***/*#//*/(/###(#*#(((###(/(((((*/(#//((/((((((#/(#///#((((#((#/(((#((///#(//##(((/((////***/////////////////*///*//////////(/////((((((//(((#####(((((((((((/*/*/*((((////////**
/*,,,**,,//**###((/(/((/(((##(((((/#((((/##(((#/(##((/#((((((((#((#%(#*///#/(/((#*######((//(///////*///(/////*/**/////,*////////////////**/((#####(#/*/(((((((/*/*///((((((///*/**,"""

# VIR-PAT

Demoa probatzeko baldintzak Python lengoaia izatea da, bere bertsioa 3.0 bertsioa baino handiago izanik eta Windows edo Linux-en oinarritutako sistema eragile bat izatea. Ondoren, deskargatzen den fitxategien artean ''requirments.txt'' izeneko fitxategia kokatu behar. Eta hurrengo komando egikaritu behar da, zure terminalean:


    pip3 install /gorde/den/direktorioa/requirments.txt


Dependentzia guztiak instalatzen diren bitartean, RASA-ren modeloa deskargatu behar da, horrela intent sailkatzailea kenduta beste zerbitzu guztiak izateko. Modelo hori Drive-en hurrengo link-an (https://drive.google.com/file/d/1TziykqonGlc_uF5-lWjf2qW4aloMrj1m/view?usp=drive_link) gordeta dago eta behin deskargatzen denean \textit{VIR-PAT/models/} direktorio barnera eramango da.

Instalazioak bukatzerakoan eta modeloa dagokion tokian jarrita dagoenean, prototipoa abiarazi daiteke. Linux-eko sistema eragile bat erabiliz gero, terminal bat ireki beharko da ''VIR-PAT'' izeneko karpetan eta terminalean hurrengo komandoa jarri behar da.


    rasa run actions & rasa shell

Windows sistema eragilea izanez gero, bi terminal ireki beharko dira, ''VIR-PAT'' karpetan ere. Baina oraingotan, komando bakoitza terminal desberdinetan jarri behar da. Adibidez, lehenengo terminalean:

    rasa run actions

Eta bigarrenean berriz:

    rasa shell

Hori eginda dagoenean, denbora bat itxaron beharko da pakete guztiak instalatzeko. Baina dena bukatzerakoan, terminalean esaldi bat sartzeko eskatuko du eta hortik aurrera pazientearekin elkarrizketa has daiteke, baina ahal den neurrian galderak bakunak eta banan banan joan behar dira, zeren txatbota sarrera bakoitzeko galdera bakar bat erantzuteko gai da. Azkenik, elkarrizketa uzteko ''\stop'' idatzi behar da terminalean. 

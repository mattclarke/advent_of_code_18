import re

real_data = """
^WSSSWNNWNENWNNWWNNWWSWNNENENWNENNWNWWNENNENNNWWWSWSEE(ENWESW|)SSWWN(E|WSWNWSWSWNWNNWSSSWSWSEEESSWWWWSSSENNEEESWSW(N|SSSESWWWSESSSEENNEEEESEESEEENNWNNWWSS(E(SEWN|)N|WNWNNE(NWWNENEENNNWSWS(E|WW(NNE(S|ENNN(WSSWNNW(N|W)|NEESWSES(W|ENE(NNWSNESS|)SEE(NWES|)(SSSWSWSW(SES(WWNNWESSEE|)E(NN|SSESESSSEEESE(NNWNWW(SEWN|)NEENNWSWNW(S|N(WS|EN))|EEEENWNEN(W|ENNW(S|WWNNEENENWNWWWWW(SSENES(ENESNWSW|)SS|NW(SWEN|)NENWNENWNENWNEEENWWWW(NNNESES(ENESESENESSEENNEENNNWWNNESENNNNEEENNNWSSWWWWWSSS(ENNESS|SWSSE(SES(ENSW|)W(SS|WWWNNWNNNWNEEEE(NWNWSWWNWWWNNNWWNWWNEEENNNEENWNNESESSESSENESSSEENESENESSWSS(ENEE(SWEN|)NWNENESSEEESWSSENENNEENESESWSWW(NEWS|)SWSEEESSESWWNNWWSSSE(NN|SSWWSEESWWWSSSSSSWWSSWNNWNWNWSSWSEE(N|ESSSENEEENN(WSNE|)ENNENWNNNESSENNESESWSSW(N|SEENEEENWW(W|NNNWNENWW(S|NENN(WSNE|)EENNENNENEEENWNWWS(WW(NENNNENNNWSSWNWWWWSWWNENWWSWWS(EESEES(WWWNSEEE|)ENEEE(NWWEES|)SE(S|N)|WW(S|NWNWNWWWWW(NENWNEENWNNEENNWNWNEEEEESWW(W|SEEEENNNW(WWWWNWNNWNENENWWWWWSSWSEEE(NWNEEWWSES|)SSS(SSWWNWSWNNWWWNEENE(SEEN(W|ESS(WW|S))|NWWWWS(WSESSEEESWSWSSENENESSSESS(ENNENE(NN(ESEWNW|)WSWNWSSE(WNNESEWNWSSE|)|SSWSS(SS|W))|WWSWSS(ENSW|)SSWWS(WSSWSSESWWWNNNWNENNWNENNNNWNEESEEEE(NE(S|E(E|N(WWWWW(SEEWWN|)WNEEENWWNEEN(WNWSWWWNWSWWNENENWWWNWSWNWNENEES(W|EEES(WW|EENENNN(ESSE(SWSSW(WWSEE(SWEN|)EE|N)|EENEEE(SWWEEN|)N(ESNW|)WWWWWSE(WNEEEEWWWWSE|))|WSSW(WNN(ESNW|)WSW(SEWN|)WWWN(EEE|WWWSWNWWSWWSEESSSEEENE(SESSEESE(NN(WW|E)|SSENEEESWSS(ENE(NENWESWS|)S|WN(N|WWWWWSWNWWWNNEENE(NWN(E|WSWS(E|WWSSWWNWSSSSWWNWWWNENWWWNNWSWSESSEE(NWES|)SESWWWWWNE(EE|NWWWNEE(NWWNWWSESSWSWNN(E|NNWWSWSESE(NN|SWSEESWWSEESEENESSESSSWWNENWNWSSWWWWNNEE(S(ENSW|)W|NWWWNWNW(SSSE(ESSWSSSENNEEESSWSESWWWSEEEEENESENNWWNEEESEEESSSENESSWWWNWW(NEENWW|SSWNWSSEEEEN(WNSE|)EEEEESEENNEEESSSSSWSESWWWNWSWWWSEESWWWWNNWNWNNN(WSSSSSSWWSSSESWWNWSWWSSWNNWSSWNW(SSSESWSEENNEEEESSWWW(NEEWWS|)SESSWNWNWWSSE(ESWSW(SSSSSENENENWN(WSSNNE|)NENESEENWNNNEESS(WNSE|)SSSWWSESWW(NNWESS|)SESWSWSWN(NENSWS|)WSW(N|SSENESESWSWW(NEWS|)SEESWSW(N|SEESSESESSSENNNNWNWNN(W|NNEEESWSS(WNNSSE|)SEEEESSENNENNNENWWNEENNENENNENWNENEESSESSWNW(SWSSWSSENENNEEESEEEESWWWSSSSSESSWSWSWWNENNE(E|S|NNNNWSSSWSWWNENWWSWW(SSSSW(WSWNWWW(NEENWW|SEESEESEEESWSEEEESSSWNWSWSWSSSSESENEESSEENENWNEENNNWNNESESEENESSSSSEESESENNENENNNNWWWNWNNWNNWWWSESE(SS(E(SESEEESSWWS(S|E|WNW(S|N(N|EEE)))|N)|WNWW(SESNWN|)WNE(E|NWWWW(NWNWW(SSE(N|E)|WN(WSWNSENE|)NENN(EE(SSS(EEESS(WNWESE|)EENWNNENESS(SEEENESEEENWNENEESEEESSWNWWSESWSESSWWS(WWNENE(E|NN(NNN|WWWWSEE(SWSNEN|)E))|ESENEENNEENNNNNNEESEENENNEEESEEEEENWNENNEEEENWWNENEENEEENWNWWNNWWN(WWWSESWWNNWSWSWSWWSEESWWWWWNNWWNEENENENWN(WWSWNN(WNWSW(SSWNWWWNWNENWWNNE(S|NENWWSWWWSWNWNEENWWNWSSSWNWSSWNNWSWNNNWSWSESWWWWWSWNWWW(SSSSSSWSSSW(N|SESWW(N|SEESSENES(EENNNE(NE(NNNENWWWWSESE(SWWNWW(NENNEEEENNESES(SEEEEESWS(WNSE|)ESWSEESW(SEENNENESSWSESESWSESWWSSW(NW(S|NNE(S|E))|SEEENEEEESWSES(WWWWSES(WWNNN(EENESNWSWW|)WWSESSSE(WNNNWNSESSSE|)|E(NEWS|)S)|ENESENNWNENNNESENNNWNWNWSSWSWNWSSSS(WNNW(SSWWSNEENN|)NNNWNNNESENNNWNNNWSSSS(E|WWNENNWSWNW(NWNWWSES(E|WWWNENWNEEN(WWWS(S|WNWSWWWNWSSSEEN(ESNW|)W)|ESEESEES(ENN(WN(WSNE|)E|EEENESSSW(NWWEES|)SES(E(SE(SSWNW(SSSW(W|S(EENNE(SS|ENNNESE(SS(WNSE|)EEEE(SSSEE(NWES|)SESWWNWSWNNW(SSSSWWSESENESENNESENN(WWWSNEEE|)EEEEENWWN(WSNE|)EEESSESSSW(SEENNENWNENWNW(NEENEN(WW(WSEWNE|)N|EEN(N|EESWSE(EE|SWWW(NEWS|)WS(SE(SW|NE)|W))))|S)|WNWSWWNW(NEE(EEESNWWW|)S|SWSW(S(E(ENSW|)S|WNWSWS(SSSSWS(E|W(N|SS))|WNW(SWEN|)N(N|EE)))|N)))|NWN(EESNWW|)W)|NN(W(NNES|SWNWS)|ESENEN))|N))|SS))|N)|N)|NN)|W))|W)))|SSESWSE(WNENWNSESWSE|)))|ENNESS(SS|ENNNE(N|E)))))|W)|W)|SSSEN(N|E(E|SS(S|WW))))|N)|S)|S)|SSSWW(NN(ESNW|)WNNWSSW(W|NNN(W|N))|SWSEENESENN(SSWNWSNESENN|)))))|NEENWWNW(NWNW(SWWWWEEEEN|)NEESENEEEEESWSEENNNEEEEEEESWSSEE(EEEES(ENESENNWWWNNWSWS(WW(NENWNWNEESE(NENWWWWWSWNNW(NEESEEN(ESENNNENEEEEESSWSWNN(WWSESSEEESWSWNWW(NNW(N|S)|SS(E(SSEEE(SSSS(WWSWN|EESS)|NN(WSWNSENE|)NE(SSEEEWWWNN|)NNE(ENWW(NNNNNENWNWWNWNWSSESWWNWNNNNNWSWWNWWNWWWWSWW(NWWNEEE(S|ENWWNWWNW(NEENWNEEEEN(EESENN(WWNEWSEE|)ESENESSSEEENNWW(SEWN|)NEEESENESEENN(ESSSSWWN(E|WSWW(NEWS|)SSWSWWNN(WWSWNN(NESNWS|)WWW(N|WWWSS(ENESS(W|ENEE(NWWEES|)SESS(WWWNE(E|N)|ESENES(ENEES(SSEENWNNESESEESWWS(WWWSSNNEEE|)SENESEESS(WNWWEESE|)EESESWWSEESENNEEESS(ENENESEEEENEN(NNWSWS(WW(SEEWWN|)NENN(NNNWSSWW(NNE(NWWEES|)S|SEESWSWWS(S|WWWNW(S|WNENWNE(NWNENWNWSWWSW(SEES(WW|SSENNNNW(ESSSSWENNNNW|))|NWNW(S|NNNEESEEEE(SWWWS(WNWNSESE|)E|NWWWNW(WWWWWSSES(E(NNWESS|)S|WW(WWWWN(WSNE|)N|N))|NEEEE(SWWEEN|)NN(ESSNNW|)WWWS(EE|WNNEEEN(ESNW|)WNWW(SEWN|)W))|E)))|EESEE(NWES|)S(WW(SE|WN)|E)))|EE))|E(S|EE))|E)|ESSWSEE(WWNENNSSWSEE|))|SSWWWW(SEWN|)N(EEENWNE(WSESWWEENWNE|)|WWWSWNNE(N(NNEWSS|)W|EE)))|W)|S)))|W))|E(S|E)))|W(S|WNWWS(WWNN(E(S|NN)|WSW(SEWN|)N)|E)))|WWWWWSW(SEWN|)NWNN(ESNW|)WSWS(S|E))|SS(EE|S(S|WWWWW(NEWS|)SSS))))|SEESESS(WNSE|)E(NENN(W(S|N(WSNE|)E)|ESE(ES(EE(NWES|)SWSESESWS(W(NN|S(SS|E))|EEEEN(WW|ENESSW))|WW)|N))|S))|W)|S))|N)|W))|E)|W)|SSS(EE|WNNWWWWSWNW(NENWNSESWS|)WS(WNSE|)ESWSEENE(S|EEN(ESNW|)W)))|S)|W)|E)|W)|SWS(WWN(NWNN(ESNW|)WWWSSS(ENENWESWSW|)SSWNWN(WW(NNWSSWN(N|W)|SSE(E|N))|E)|E)|E))|SS)))|N)|E)|EEE(SEE(E|SWWS(E|W(WS(SW(SEWN|)N|EE)|NN)))|NN))|EENEEEENENNESESSENESEENNW(WWNWNENESES(W|EESSESESWW(N|WWSSWSWSSWWSSSWWWWSESSWNWNW(SWSSSSWWW(SWNWWSESWSSSSSSSSEEESENNWNEEEESESWSSSSENENN(WSNE|)NEESESWSW(NN|SWSSSESWSWNWNENWN(E|WSWSSWWNWNWWWNNWWSSSWWWSSSWNWNWSWWWWNNEES(ENNWWWNNWNNNWSSSW(NNNNEEESESWSEENESSS(WNWSNESE|)ESEE(EEENWNWWNEENWNNNNNESEEENE(SSWWSSENESSWS(EENESSENEN(WNWWEESE|)ESSS(ENNE(NNW(NNESNWSS|)S|S)|S(WN(WWWNSEEE|)N|S))|WW(S|N(NNW(NEWS|)S|E)))|NNNWNWSSESWW(SEWN|)NWWNWSWSWSESSSSS(ENNNNNNEE(WWSSSSNNNNEE|)|SW(SESEEWWNWN|)NNNWNN(ESNW|)N(WSSS(SEWN|)WN(WW|NN)|NNENNW(N(EES(S|ENESENN(NNESSS(SSWENN|)ENESE(NNWWEESS|)S|W))|N)|S))))|S(S|WW))|SSSSSWWSEESWSSEEN(NNNNE(SSEESSENNESESWSESENNN(NWES|)EESENEENWNN(WSSNNE|)ESESSSWWSWSWNW(SSEEENENEESENNESSSWSWSWSEES(WWWWNWWS(WWNENN(WNWWNWNWWSW(NNNESNWSSS|)WSWNWSWNWWSWWWSEEEE(SSEES(EEEEEEENE(S|N(E|WWSWNNWN(WSWWS(WNWSNESE|)ES(ENESNWSW|)W|E(ESEEWWNW|)N)))|WWWNWN(E|WWWNWWWSSS(WNNNWSSWS(WWNNE(S|NWWWNWSWSWWWWWSEES(EEN(ESEEENWWNEE(WWSEESNWWNEE|)|W)|WWWWNNE(NNEENNWWNWWSSWSSWW(SESEE(SWWWNSEEEN|)N(W|NNE(S|N(EE|N)))|NENNW(S|NNEE(S(S|W)|NENWWNW(SSEWNN|)NENNW(NEESESSES(WWNNSSEE|)EENNNNWNWS(WNWNNWSW(SEWN|)NNNNNNESENNNNNE(NWNWW(NNESNWSS|)SSSSE(SWEN|)NNN|SSEEEE(NWES|)SESSWWWWSSESWSEES(WWWNNWWNNEE(SWEN|)NNNESEE(NWES|)E|SENEENNNWWS(SENSWN|)WNN(W|EEENESSE(SWSSSSE(SESWSSWWWSSWWWS(W(W|NNEEENNNESENN(ESSNNW|)NW(NE|WSE))|ESEEN(W|ENNEEEENN(WSNE|)EE(SSEEEENWN(WSWNSENE|)EESSSENNENENN(EESESSSEE(NEN(WWSNEE|)NNE(SSS|N)|SSESSWNWWS(E|WS(E|WNNNWSWSWSS(EEN(N|W)|WNNNEN(ENNESENN(W|N(N|ESSSS(EENWESWW|)S))|WWSWSESSWNWNNNN(E(E|S)|WSWSESWWS(SENESESS(NNWNWSNESESS|)|WWNNE(S|NE(N(NN|WWWWSE(SWWSWSESWS(EENENWNE(WSESWSNENWNE|)|WW)|E)|E)|S)))))))))|NNWW(SSW(S(W|E(ENNSSW|)S)|N)|NNESEN))|N(N|WW))))|NNN)|ENN(E(EE|S)|W(S|NNWW(SE|NW)))))))|SES(S|W))|S))))|S)))|E)|EEEEN(ESE|WWWNE))))|N)|ESENEE(EN(N|E|W)|S(S|W)))|E)|ENN(NEESESWW(N|SEEENNESES(W|EEEEEENNNWSWNWSWNWNEEEENEEEEESSWSWSS(ENESENESEEENENEENEEENNESESENESSWSES(WWNWN(WSS(WWWW(NEENES|W)|E)|N|E)|ENNEENWWNENWWNENNNESENNWWWNWSSWSSE(SSWNWWWWSS(ENSW|)WNNWNWSWNNWSWNNWNENESES(W|EENWNWNENNNWNENESESENESSWWSW(NN|SES(W|SEENEES(SW(N|WSS(ENESNWSW|)WNW(NEWS|)(S|WW))|ENNNWSWN(NENNEESWSEESS(WNSE|)ESENENESS(EEESWSSSENESSEEESENNENENNWSWWNNNWNNWNEENNNWWSWS(EENSWW|)SWWSESWW(NWWNWSW(SEWN|)NWNENEENEESS(SWN(N|WW)|EENNENEENWNWSWSW(SS|NNENWNWSWSSE(SWWNNNNWSSWNNWNWSSWWSSWWNENNWWS(SSSSES(WWNWWWNWWNWNWWWSSSWSWW(SWSWSS(WNSE|)SENNEEESEENWNEEEENE(SSWWSES(ENENSWSW|)WSWN(WWWSSESEN(NWES|)ESSWSS(ESESWSES(ENENWNE(NWWN(W|N)|EEESWWS(SWSWENEN|)EE)|WW)|WNNWSWWNEN(NNW(NENWESWS|)SSWNNWSSSESWS(EEEE|SWNWSWWNENWWWWWW(NEEENWN(EE(NN|SSEEEE(SWEN|)N(WWWNSEEE|)N)|WSWWWNW(NEN(ESSENSWNNW|)WW(S|NN)|SS(S|EE)))|SEESWS(WNSE|)EES(EE(SESEEEE(WWWWNWESEEEE|)|NWNWNE)|W)))|E))|NN)|N(WWSWNNE(EE|NWNWSSSWS(WSW(W|N)|E))|E))|NENENNWWNNNESEEENNWNNNWNWSWNNNEENNNNNESSEEESENEENESEEEESEEEENWWWNWWWWNEENWWNENWNWWSESSWNWWNNWNN(WSSSESWSW(SSEEN(W|ESEN(NWWEES|)EE)|W(WWSSSSWNWWSSSE(SWSSSSSSE(SWWWNWWWNWWNWN(WSSESESE(S(WWWN(W(SSESWENWNN|)N(NN|E)|E)|ENESE(N|SEEES(WW|E(SENE|NNWWW))))|N)|EEN(W|ESES(WW|ENNWNNNNESEESSSSSS(W(NNNNNWS(NESSSSNNNNWS|)|WW)|S))))|NEEE(SEWN|)NWWWN(NN|EEE))|N(EE|N))|NNE(N|S)))|ESE(SS|EN(NNEENESSWSW(SEEES(SEEENWNNNWNNW(SSS(ESSNNW|)W|NNWWNENWNWSWSSWNNNNNWWWSSS(WNNWNENWNNEES(ENNESENNN(ESSEESEEENESENNWWNEEESSEESSSWNW(NEWS|)WWWSWWSWWS(EESEENN(WSNE|)EEE(NWWEES|)SSSWSESEEEENWWWNNENEN(WWSNEE|)EENWNW(S|NNENNWNWNNWSWNNNNNENNNNNWSWNNWWN(WWSSWW(NENSWS|)SWSSWS(WNSE|)SSEENENW(WSNE|)NNEES(SSSSESENNNW(S|NNEEEN(WNWW(SEWN|)(N(EE|N)|WW)|ESSWW(W|SESWSSE(N|SSWWN(E|WWSWSSEE(SSWNWWNNNNWNN(WSSNNE|)ESE(NN|S|E)|N(W|EEEEESSE(N|E)|N)))))))|W)|NNENWNNNWWW(SS(ENESS|WN)|NENNESSENNENWWWW(SS|WWWWS(E|WNWSWNNNWWWNWWNNEEES(SEEENWNEESEEESESES(WWNWSWWN(WSNE|)EN(E|W)|ENNWNWNNWNWSW(SEEWWN|)NNWWNWWSWWSWNNENNWNNWWNWNWNN(EES(W|SEENN(WSNE|)EEESWWSEESEEENNWN(WSSEWNNE|)EESEEN(W|EESESEESEESSWNWSWSSWWSWNNEENNENWWWSESWWNWW(WWWSSENESS(ES(ESE(EEESW(W|SSENENNEN(NESSSSW(SESWSEENNNESEENENWW(WNW(NENWN(ENENENESENNWNWSWW(WNN(WS(S|WNW(S|W))|ESENEEEES(ENESENESENESSEENWNEEEEESENEEESSWW(NEWS|)SEEE(NNN|SWWWSESENESSSSSWSWWNENWNWWNEN(ESEES(S|W)|NNWNENWWNWSW(N|SEESSS(ENSW|)SWNWSWWSEEESWSSSSESESEESENEESSW(N|WWSWSSENENEEE(SWWSESWSWN(WSWSEEESSENE(NN(WSNE|)NN|SSWSWWSWNNE(E|NWN(WWNNN(E|NNWWNNWNWSSWSSSESSWNWNNWWWWNWNNWWSWSWSSEESEEN(EESENESSWWW(WSSWWNN(ESNW|)WWSESWSWW(NNNNNE(S(EE|SSS)|NNW(NEENENEENEES(ESENESSE(NNNE(SS|EEE(NWWNWWS(WNWWS(WNNNENEENWNENENWNNEEEE(S(ENESNWSW|)WW(S(SSWSESSW(N|WS(EEEE(NWNENW|S)|W(W|N)))|EE)|W)|NWWWNWWWWWSEEE(SWWWSEESS(ENNSSW|)WSESWWW(WNENWNN(ESE(E|SS)|WSSSW(SEWN|)NN)|SE(SSW(SESWWN(N|WWWSES(E(E|N)|SWNWWWS(EESEWNWW|)WNNN(N|W)))|N)|E))|E))|ES(W|E))|E)|ES(W|ES(SWN|EN))))|SWWWN(WNSE|)E)|W)|WS(E|SSS)))|S(WNSE|)ESEESENENWW(NEEEESSSW(NN|SEESWWSEEEESESWWWWWN(WSWNNW(NEE(S|N(WW|N))|SSSEEESWSESWW(NNWSWNN(SSENESNWSWNN|)|SESEEN(NNNESENEEEESSSESWWWNNW(NEESSNNWWS|)SWSW(NNEWSS|)SWSEESESSEENWNNWN(W|N|EESENESESSSSESWWNW(WWWSWSWSSWW(SEEEENN(WSNE|)EESSW(SWWSESWSESWSWNWWNWNWSSWWSWS(WNNNWNEEES(WSNE|)ENN(WWWWN(NW(SS|WNEENNES(NWSSWWEENNES|))|E)|EEESENE(NWW|SSW))|SEESENNEN(WWSWENEE|)(ESE(N|ESWSWSESWWSWNN(ENNEWSSW|)WSWSS(WWNWWNEN(ESE(NNESNWSS|)S|WW)|E(EEESESEEEEESWWSWSWNWN(EE|WWSESESWWWWSESESEENN(W(S|W)|EESEESESEEESWSEESEEEEEEE(SWSESWWNNWSSSWWWNNEN(ESSWENNW|)WWSSW(WNENWN(E|W(S|WWNN(ESENSWNW|)W(S|WNW(N(EESEWNWW|)N|WS(WNWSWNNWWWWWSWS(WWWNENWWSWNWNENNNENWWN(EN(ESESENE(NWWEES|)SEEESSSS(EE(E|NWNNE(ENN(E(SSEWNN|)NN(WS|ESE)|WSWNWWW(EEESENSWNWWW|))|S))|WWW(WWNN(WSSNNE|)EN(EESWS(EENNSSWW|)W|W)|S(S|E)))|W)|WWSESWSSSWNNNWW(WW|NEENNWSWN(SENESSNNWSWN|)|SESSSEESE(NNNEN(N|W)|ESWSS(WNNW(SSWWWW|N)|ES(SEESENE(S|NNWSWWNEN(NWSWENES|)EE)|W)))))|EESENN(EE|W))|E|S)))))|SSSSEEENEN(WWW(SEWN|)N|EESESWW(WSEESWWSSSSSW(SWSWSESWSSSS(WNWNWNEE(NWWNWWSSWNNNWSWNNNW(NENWESWS|)SSSS(SENESSESENE(SS(E(N|E)|WWWWN(NWSWWSEE(WWNEENSWWSEE|)|E))|NN)|WNNWNE)|S)|EEENEENWWWN(WSSEWNNE|)ENEES(ESE(SSW(N|WW)|NNNW(WNEENWWW(SW(N|WS(EE|S))|NENEE(SWEN|)NNWN(ENWNENNNNW(W|S)|WWSES(WSNE|)E))|S))|W))|NNNNNWWW(WNEEEE|SS(EENWESWW|)S))|N)))|NNNWNENNNWWNNESENNNNNNWSSWNNWWSWSSSSWWSSWWNNW(SSWNW(NEWS|)SS(EES(W|ENESS(WW|ESSEENNEEE(SSESWWNNWSSWW(EENNESNWSSWW|)|NWWNWW(NEEE(SEESNWWN|)NNNW(SSWWEENN|)NNE(SESENSWNWN|)N|WSE(SS|E)))))|WN(N|WW))|NNENEESS(ENNNWWWWNWWNENNNNEESWSSSEES(EENWNNENWNW(SSWSEWNENN|)NWNNWNWW(SSE(N|ESWWSW(SW(SSE(SSWSW(WN(EN(E|NN)|W)|SEENEES(E|W))|EN(W|N))|N)|N))|NEEEENWW(W|NNESENNWN(EESEESSSSWNNW(NEWS|)SSSESWS(WNNWESSE|)SEES(W|SSS(W|S(S|EEEENNE(NNNWSSWSWS(E|WNNENNNE(EENWWWWW(NEENNNW(NNESEENE(SSSSWW(SEE|NENW)|NWW(WNENEE(SWEN|)NWNWNWNNNWNWNWSWNNNNWW(SSE(N|S(W|SSES(W|ESWSSSESEE(SSWWNE|EN(NWW(SEWN|)WNENE(NWNWESES|)S|E)))))|NEEESENESSEEESE(SSSWNNWW(N(E|W(WNWSNESE|)S)|SESSSENESS(W|S))|NNNWWW(SEEWWN|)NENNESSENNNWWWN(ENEE(SWEN|)N|WWSSWNNNNE(S|NNWWNNNWW(NN(EESWENWW|)N(WSNE|)N|SSSWWSESSWSSESWS(ES(WSS(ENSW|)WWWWW|EENWNEE(SSENEE(SWEN|)N(ESNW|)N|NNWW(SEWN|)(W|NNEN(NNN|W|E(SSWENN|)E))))|WNWWNEENNN(E|NWWNEN(E(N|EE|S)|WWS(WNSE|)SSSSENNESS(NNWSSWENNESS|)))))))))|S))|SS)|S(ESSNNW|)W)|SS))|SS))))|W(NWWS(E|W)|S))))|W)|W(SS|N|W))))))|N)))|N))|N)|NEN(NNE(S|ENWN(E|NWSW(SEWN|)(W|NNN)))|WWSWS(E|W)))|NNN(ESSNNW|)W))|W)))|EEE))|W))|N)|WN(E|W(NENSWS|)W)))|E)))|N)|NNNNWNWWS(E|WNN(EEEE(S|N)|NWNENWW(SWSES(W|SE(S|N))|N))))))))|W))|S(E|S))|WW)|S)|S)|N)|WW))|NNNW(WNEWSE|)S)|W)|WWWW(S|NNWNE(ESS|NWWW)))|NEEN(WW|E(E|N)))))|WSW(N|SWSEE(N|SW(SEEE(NWNSES|)EESS(E|SSSS(EEEE(N(E(N|ES(ENSW|)W)|W)|SS)|WWWN(WWSESEEESWWWSSWNW(SWSEEEEEEN(NWWSEWNEES|)ESSE(SWW(S|WN(W|E))|EN(WN|EESW))|NN(ESNW|)W)|EE)))|W)))))|WW))))))|W(S|NNEEN(EE|WNWSWWS(WW|E))))|WSWWSWNW(N|SWSSWSSWSWSSS(WWNWSW(SSS(WNSE|)EENENWWS(NEESWSNENWWS|)|NNENW(WSWWEENE|)NEN(EES(ENENWESWSW|)SW(SESNWN|)N|NNNWWWNWNENENN(EENEN(ESESE(SWW(WNE|SEE)|NNNW(NW(NEEE(SWEN|)NNE(SEWN|)NNNW(NEWS|)WWWSSESWSEENNENWW(EESWSSNNENWW|)|S)|S))|W)|WSWWS(WNW(SSEESWSW(N|SEEE(NWES|)EEES(W|S))|NEENES)|E))))|ENNE(S|E(E|N(W|NN))))))|W)|ENNESSS(SSEEE(SWWEEN|)(NN|EE)|WW)))|W)|N)|W))))|E(NEEENW(WWW|NEN(W|E(N|SSS(SWWWEEEN|)EENNWS)))|SS))|E)|N)))|SEEESE(NNWNSESS|)SWS(EE(SWSEENE(WSWWNEWSEENE|)|NN)|W))|W)|WWS(S|E))))))|NE(N|S)))|WNNNEN(E|WW))))|W))|N)|NWNNES)|W))|W)))|NNNNESSSENNN(SSSWNNSSENNN|))|NN(E(S|EN(W|ESEENNW(S|NNNNWWW(SEESNWWN|)NEEEENE(N|SESS(ENNESNWSSW|)SSWNW(NNESNWSS|)S))))|W))))|S)))|W)|W(NN|W))|E)|W(NEWS|)S))|SEESWSSSSWWSS(E(NEENSWWS|)SS|WNWW(SEWN|)NEEN(EENNNSSSWW|)W))))|N))|NN)|NENEN(WNNSSE|)EEE(N(W|EN(WNE|ES))|S(S|WW))))|NN))))|N)|N)|NNNENWNENNESSSSENEENEE(NWWNWSW(SEWN|)NNWWNNENESEEEEN(NWWW(SEEWWN|)NEEENWN(WWWWWSSW(NNNNN(E(EENNEWSSWW|)SS|NNNNNE)|SE(EENN(WSNE|)EE|SWSSSSS(NNNNNEWSSSSS|)))|EEE)|ESE(SWWSEESSWNWWNNWW(SEWN|)WW|N))|SSW(N|WWS(WWWSNEEE|)E)))|ESENNEEESSWW(NEWS|)SS(WNWESE|)(SS|EEN(W|E(S|ENWNEESE(NNNESSS(NNNWSSNNESSS|)|S(S|W)))))))|N)|NNESEE(NWN(WNENNENWWW(SESWSS|NNEEES(EENEENWNEESSEENNNW(NEEESSW(SSSWWWS(WW(NEWS|)WW|EESENENNEN(W|NNEEENEENN(WWS(WWN(WWWWWS(EEEESEE(WWNWWWEEESEE|)|WSWS(WNNWN(WSWNWWSSW(NN|SEEN(N|EESSS(ENNNSSSW|)(S|WN(N|WSWNWS))))|EE(S|E))|E))|E)|E)|EEESSWW(NEWS|)SESWSSENENESSWSES(WWWN(E|WNNNNWSSSWSW(SES(W|EE(NWNSES|)ESS(WNSE|)E(NN|S))|W(NNE(S|N(ESNW|)W)|W)))|E(NNNE(SSENEWSWNN|)NNW(W(NNNEEWWSSS|)W|S)|S)))))|N)|SS)|WW))|E)|S(S|W))))))|E))))|ESS(EN(ESNW|)N|W(WW|N))))))|NN(ENWESW|)WSWSWNN(N|E)))|S))))|E)|N)))|SWWSEESSWWWN(NNWSSSSE(E|SSW(SSS|N))|EE))|EE))|EE))|E(NN|E))|SS))|SEESS(S|EEE(NWWNEWSEES|)E))))|WS(WW|E(SWSEWNEN|)E))|E))))))|WNWWS(ESNW|)WNWWWW(SEEESNWWWN|)NEENN(WWS(E|W(NNNESEN(SWNWSSNNESEN|)|W))|ESSEEEE(WWWWNNSSEEEE|)))|SWWSSE(SSEWNN|)N))|N))|W)|SS(WNSE|)S))))))|NNNE(N(ESNW|)W|S))|E))))|S(E|SSW(WNENSWSE|)SEESWS(W(WWSSNNEE|)N|E))))|S))))$
"""


class Node:
    def __init__(self, name):
        self.nodes = []
        self.name = name
        self.min = float("inf")
        self.max = 0


def parse(data, index):
    chunk = ""
    while index < len(data):
        c = data[index]
        if c in ["N", "W", "S", "E"]:
            chunk += c
        elif c in ["(", ")", "|"]:
            if len(chunk) > 0:
                return chunk, index
            else:
                return c, index + 1
        index += 1
    return chunk, index


def test(root, data, index):
    nodes = []
    carry = []
    while index < len(data):
        c, index = parse(data, index)
        if c == ")":
            return index, nodes
        elif c == "|":
            if data[index] == ")":
                nodes.append(root)
            carry = []
        else:
            if not carry:
                n = Node(c)
                root.nodes.append(n)
                nodes.append(n)
                if data[index] == "(":
                    # print("Dip in")
                    index, carry = test(nodes[-1], data, index + 1)
                    # print("Dip out")
            else:
                n = Node(c)
                for i in carry:
                    i.nodes.append(n)
                carry = []


def get_strs(root_node):
    answers = []

    def _get(stored, node):
        if len(node.nodes) == 0:
            line = 0
            for s in stored:
                line += len(s.name)
            # print(line)
            answers.append(line)
        else:
            for n in node.nodes:
                stored.append(n)
                _get(stored, n)
                stored.pop(-1)

    stored = [root_node]
    for n in root_node.nodes:
        stored.append(n)
        _get(stored, n)
        stored.pop(-1)
    return answers


def find_best_answer(answers):
    longest = None
    count = 0

    # Find longest
    for a in answers:
        length = len(a) - a.count(" ")
        print(a, length)
        if length > count:
            longest = a
            count = length

    # Now find answer
    last = longest[longest.rindex(" ") :]
    shortest = longest

    for a in answers:
        if a.endswith(last):
            length = len(a) - a.count(" ")
            if length < count:
                shortest = a
                count = length
    return shortest, count


def solve(data):
    first, index = parse(data, 0)
    root = Node(first)
    root.min = len(root.name)
    root.max = len(root.name)

    nodes = []
    curr = root
    while index < len(data):

        c, index = parse(data, index)
        if c == "(":
            index, nodes = test(curr, data, index)
        elif c == "" or c == ")":
            pass
        else:
            temp = Node(c)
            for n in nodes:
                n.nodes.append(temp)
            curr = temp

    return root


NODES = set()


def do_count(root_node):
    NODES.clear()

    def _get(node, count):
        count += len(node.name)

        if len(node.nodes) == 0:
            node.min = min(node.min, count)
            node.max = max(node.max, count)
            NODES.add(node)
        else:
            for n in node.nodes:
                _get(n, count)

    count = len(root_node.name)
    for n in root_node.nodes:
        _get(n, count)


def get_max_min(nodes):
    max = 0
    min = 0
    best = None

    for n in nodes:
        if n.max > max:
            max = n.max
            min = n.min
            best = n
    return min, max, best


test_1 = """^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$"""
root = solve(test_1)
do_count(root)
ans, max_len, bn = get_max_min(NODES)
assert ans == 18
assert bn.name == "NNN"

test_2 = """^ENWWW(NEEE|SSE(EE|N))$"""
root = solve(test_2)
do_count(root)
ans, max_len, bn = get_max_min(NODES)
assert ans == 10
assert bn.name == "EE"

test_3 = """^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$"""
root = solve(test_3)
do_count(root)
ans, max_len, bn = get_max_min(NODES)
assert ans == 23
assert bn.name == "NNNE"

test_4 = """^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$"""
root = solve(test_4)
do_count(root)
ans, max_len, bn = get_max_min(NODES)
assert ans == 31

root = solve(real_data)
do_count(root)
ans, max_len, bn = get_max_min(NODES)
print(ans)

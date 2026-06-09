# Definition Codebook

As each definition of antisemitism provides unique guidelines and examples as to what constitutes antisemitism, the dataset is labeled to identify what specific components of the definition may apply to a given text. These codes are returned as 0 (Not Applicable), 1 (Explicitly Applicable), 2 (Implicitly Applicable), or 3 (Ambiguous).

## Code Map

| Concept | IHRA | Nexus | JDA |
|---|---|---|---|
| Collective blame | E11COLLECTIVEBLAME | N4COLLECTIVEBLAME | B7COLLECTIVEBLAME |
| Collective guilt via symbols/images | — | N8COLLECTIVEGUILT | B6ISRAELCARICATURE |
| Conspiracy / hidden Jewish power | D2CONSPIRACY, E2CONSPIRACY | N3CONSPIRACY, N5HIDDENCONSPIRACY | A2CONSPIRACY, A2HIDDEN |
| Control of media | E2CONTROLMEDIA | N3CONTROLMEDIA | A2CONTROLMEDIA |
| Control of economy | E2CONTROLECONOMY | N3CONTROLECONOMY | — |
| Control of government | E2CONTROLGOV | N3CONTROLGOV | A2CONTROLGOV |
| Control of other institutions | E2CONTROLOTHER | N3CONTROLOTHER | — |
| Double standard applied to Israel | D2DOUBLESTANDARD, E8DOUBLESTANDARD | N13DOUBLESTANDARD | C15DOUBLESTANDARD |
| Loyalty / fifth column trope | E6ISRAELFIFTHCOLUMN, E6GLOBALFIFTHCOLUMN | N6LOYALTYDOUBT | A2FIFTHCOLUMN, B9ISRAELFIFTHCOLUMN |
| Denial of Jewish self-determination | E7JEWISHRIGHTS | N11SELFDETERMINATION, N12ADVOCATEDENY, N12SELFDETERMINATION | B10JEWISHRIGHTS |
| Israel as racist endeavor | E7ISRAELRACIST | — | — |
| Holocaust denial | E4HOLOCAUSTDENIAL | — | A5HOLOCAUSTDENIAL |
| Holocaust minimization | E4HOLOCAUSTMINIMIZE | — | A5HOLOCAUSTMINIMIZE |
| Holocaust mechanism denial | E4HOLOCAUSTMECHANISM | — | A5HOLOCAUSTMECHANISM |
| Holocaust exaggeration accusation | E5HOLOCAUSTEXAGGERATE | — | — |
| Nazi comparison | E10ISRAELNAZI | — | — |
| Classic antisemitic symbols applied to Israel | E9CHARACTERIZEISRAEL | — | B6ISRAELCARICATURE |
| Requiring Jews to condemn Israel | — | — | B8FORCECONDEMN |
| Treating Jews as Israeli agents | — | — | B7ISRAELAGENT |
| Physical harm / violence | E1VIOLENCE | N9PHYSICALHARM | A3ASSAULT |
| Incitement to violence | — | N10INCITEMENT | — |
| Stereotyping | D2STEREOTYPE, E2STEREOTYPE | — | A1ESSENTIAL |
| Dehumanization | E2DEHUMANIZATION | — | — |
| Demonization | E2DEMONIZE | — | — |
| Blame for world's problems | D2BLAME | N5ISRAELHAND | — |
| Jewish identity denial | — | N7IDENTITYDENY | — |
| Discrimination | E14DISCRIMINATION | N1DISCRIMINATION | A3EMPLOYMENT |
| Criticism of Israel not antisemitic | D2DOUBLESTANDARD | N14ISRAELCRITICISM | C13ISRAELEVIDENCE, C13ISRAELPOLICIES |
| Opposition to Zionism not antisemitic | — | N17OPPOSITION | C12ZIONCRITICAL |
| BDS not antisemitic | — | N14ISRAELCRITICISM | C14BDS |
| Harsh/disproportionate criticism not antisemitic | — | N16HARSHCRITICISM, N18DISPROPORTIONATE | C15REASONABLE |
| Palestinian rights / justice not antisemitic | — | — | C11PALESTINIANJUSTICE, C11PALESTINIANRIGHTS |
| Suppression of criticism via antisemitism accusation | — | N15SUPPRESSIONFREEDOM, N15SUPPRESSIONDIALOGUE | — |

## [International Holocaust Rememberance Alliance (IHRA) Working Definition](https://holocaustremembrance.com/resources/working-definition-antisemitism)

1. Definition (YES Codes)

   1.1 D1
   - D1PERCEPTION "Antisemitism is a certain perception of Jews"
   - D1HATE "which may be expressed as hatred toward Jews."
   - D1MANIFEST "Rhetorical and physical manifestations of antisemitism are directed toward Jewish or non-Jewish individuals and/or their property, toward Jewish community institutions and religious facilities."

   1.2 D2
   - D2ISRAELTARGET "Manifestations might include the targeting of the state of Israel, conceived as a Jewish collectivity."
   - D2DOUBLESTANDARD "criticism of Israel similar to that leveled against any other country cannot be regarded as antisemitic."
   - D2CONSPIRACY "Antisemitism frequently charges Jews with conspiring to harm humanity"
   - D2BLAME "it is often used to blame Jews for 'why things go wrong.'"
   - D2STEREOTYPE "employs sinister stereotypes and negative character traits."

2. Contemporary examples of antisemitism (YES Codes)

   2.1 E1
   - E1VIOLENCE "Calling for, aiding, or justifying the killing or harming of Jews"
   - E1RADICAL "in the name of a radical ideology or an extremist view of religion."

   2.2 E2
   - E2ALLEGATION "Making mendacious ... allegations about Jews as such"
   - E2DEHUMANIZATION "dehumanizing ... allegations about Jews as such"
   - E2DEMONIZE "demonizing ... allegations about Jews as such"
   - E2STEREOTYPE "stereotypical allegations about Jews as such"
   - E2COLLECTIVEAGENDA "the power of Jews as collective"
   - E2CONSPIRACY "the myth about a world Jewish conspiracy"
   - E2CONTROLMEDIA "Jews controlling the media"
   - E2CONTROLECONOMY "Jews controlling the economy"
   - E2CONTROLGOV "Jews controlling the government"
   - E2CONTROLOTHER "Jews controlling other societal institutions."

   2.3 E3
   - E3COLLECTIVEBLAME "Accusing Jews as a people of being responsible for real or imagined wrongdoing committed by a single Jewish person or group, or even for acts committed by non-Jews."

   2.4 E4
   - E4HOLOCAUSTDENIAL "Denying the fact ... of the genocide of the Jewish people"
   - E4HOLOCAUSTMINIMIZE "Denying the ... scope ... of the genocide of the Jewish people"
   - E4HOLOCAUSTMECHANISM "Denying the ... mechanisms (e.g. gas chambers) ... of the genocide of the Jewish people"
   - E4HOLOCAUSTINTENT "Denying the ... intentionality of the genocide of the Jewish people"

   2.5 E5
   - E5HOLOCAUSTINVENT "Accusing the Jews as a people, or Israel as a state, of inventing ... the Holocaust."
   - E5HOLOCAUSTEXAGGERATE "Accusing the Jews as a people, or Israel as a state, of ... exaggerating the Holocaust."

   2.6 E6
   - E6ISRAELFIFTHCOLUMN "Accusing Jewish citizens of being more loyal to Israel"
   - E6GLOBALFIFTHCOLUMN "or to the alleged priorities of Jews worldwide"

   2.7 E7
   - E7JEWISHRIGHTS "Denying the Jewish people their right to self-determination"
   - E7ISRAELRACIST "claiming that the existence of a State of Israel is a racist endeavor."

   2.8 E8
   - E8DOUBLESTANDARD "Applying double standards"
   - E8UNIQUEDEMAND "requiring of it a behavior not expected or demanded of any other democratic nation."

   2.9 E9
   - E9CLASSICSYMBOL "Using the symbols and images associated with classic antisemitism"
   - E9JESUSKILLING "claims of Jews killing Jesus"
   - E9BLOODLIBEL "blood libel"
   - E9CHARACTERIZEISRAEL "Using the symbols and images associated with classic antisemitism (e.g., claims of Jews killing Jesus or blood libel) to characterize Israel or Israelis."

   2.10 E10
   - E10ISRAELNAZI "Drawing comparisons of contemporary Israeli policy to that of the Nazis."

   2.11 E11
   - E11COLLECTIVEBLAME "Holding Jews collectively responsible for actions of the state of Israel."

3. Additional Enforcement (YES Codes)

   3.1 E12
   - E12CRIMINAL "Antisemitic acts are criminal when they are so defined by law"
   - E12CRIMINALDENIAL "for example, denial of the Holocaust"
   - E12CRIMINALMATERIAL "or distribution of antisemitic materials in some countries."

   3.2 E13
   - E13TARGET "Criminal acts are antisemitic when the targets of attacks ... are selected because they are, or are perceived to be, Jewish or linked to Jews."
   - E13PEOPLE "whether they are people"
   - E13PROPERTY "or property"
   - E13BUILDINGS "such as buildings"
   - E13SCHOOLS "schools"
   - E13WORSHIP "places of worship"
   - E13CEMETERIES "cemeteries"

   3.3 E14
   - E14DISCRIMINATION "Antisemitic discrimination is the denial to Jews of opportunities or services available to others"

4. NOOTHER_I: Text is not antisemitic and does not fit the IHRA working definition.

## [The Nexus Document](https://nexusproject.us/nexus-resources/the-nexus-document/)

1. General Definition (YES Codes)

   1.1 N1
   - N1BELIEFS "anti-Jewish beliefs, attitudes, actions or systemic conditions"
   - N1NEGATIVEATTITUDE "negative beliefs and feelings about Jews"
   - N1HOSTILECONDUCT "hostile behavior directed against Jews (because they are Jews)"
   - N1DISCRIMINATION "conditions that discriminate against Jews and significantly impede their ability to participate as equals in political, religious, cultural, economic, or social life."

2. Israel and Antisemitism: What Is Antisemitic (YES Codes)

   2.1 N2
   - N2STANDARD "Whether speech or conduct about Zionism and Israel is antisemitic should be based on the standards for speech or conduct that apply to antisemitic behavior in general."

   2.2 N3
   - N3CONSPIRACY "Characterizing Israel as being part of a sinister world conspiracy of Jewish control of the media, economy, government or other financial, cultural or societal institutions."
   - N3CONTROLMEDIA "Jews controlling the media"
   - N3CONTROLECONOMY "Jews controlling the economy"
   - N3CONTROLGOV "Jews controlling the government"
   - N3CONTROLOTHER "Jews controlling other financial, cultural or societal institutions."

   2.3 N4
   - N4COLLECTIVEBLAME "Holding individuals or institutions, because they are Jewish, a priori culpable of real or imagined wrongdoing committed by Israel."

   2.4 N5
   - N5HIDDENCONSPIRACY "Indiscriminately blaming suffering and injustices around the world on a hidden Jewish conspiracy"
   - N5ISRAELHAND "or of being the maligning hand of Israel or Zionism."

   2.5 N6
   - N6LOYALTYDOUBT "Considering Jews to be a priori incapable of setting aside their loyalty to the Jewish people and/or Israel."

   2.6 N7
   - N7IDENTITYDENY "Denigrating or denying the Jewish identity of certain Jews because they are perceived as holding the 'wrong' position (whether too critical or too favorable) on Israel."

   2.7 N8
   - N8COLLECTIVEGUILT "using symbols and images that present all Jews as collectively guilty for the actions of the State of Israel."

   2.8 N9
   - N9PHYSICALHARM "attacking and/or physically harming a Jew because of her/his relationship to Israel."

   2.9 N10
   - N10INCITEMENT "conveying intense hostility toward Jews who are connected to Israel in a way that intentionally or irresponsibly... provokes antisemitic violence."

   2.10 N11
   - N11SELFDETERMINATION "treating Israel in a negative manner based on a claim that Jews alone should be denied the right to define themselves as a people and to exercise any form of self-determination."

   2.11 N12
   - N12ADVOCATEDENY "advocating a political solution that denies Jews the right to define themselves as a people"
   - N12SELFDETERMINATION "denying them — because they are Jews — the right to self-determination"
   - N12PHYSICALSAFETY "and/or the right to physical safety and full human, civil, and religious rights."

   2.12 N13
   - N13DOUBLESTANDARD "treating Israel differently solely because it is a Jewish state, using standards different than those applied to other countries."

3. Israel and Antisemitism: What Is Not Antisemitic (NO Codes)

   3.1 N14
   - N14ISRAELCRITICISM "criticism of Zionism and Israel, opposition to Israel's policies, or nonviolent political action directed at the State of Israel and/or its policies should not, as such, be deemed antisemitic."

   3.2 N15
   - N15SUPPRESSIONFREEDOM "Using accusations of antisemitism as a tool to suppress criticism of Israel infringes on the principle of freedom of expression"
   - N15SUPPRESSIONDIALOGUE "and militates against constructive dialogue and debate among people with differing opinions."

   3.3 N16
   - N16HARSHCRITICISM "Even contentious, strident, or harsh criticism of Israel for its policies and actions, including those that led to the creation of Israel, is not per se illegitimate or antisemitic."

   3.4 N17
   - N17OPPOSITION "Opposition to Zionism and/or Israel does not necessarily reflect specific anti-Jewish animus nor purposefully lead to antisemitic behaviors and conditions."
   - N17NATIONALISM "opposing the principle of nationalism or ethnonationalist ideology"
   - N17ADVERSEEXPERIENCE "someone's personal or national experience may have been adversely affected by the creation of the State of Israel."

   3.5 N18
   - N18DISPROPORTIONATE "Paying disproportionate attention to Israel and treating Israel differently than other countries is not prima facie proof of antisemitism."

4. NOOTHER_N: Text is not antisemitic and does not fit the Nexus Document definition.

## [Jerusalem Declaration on Antisemitism](https://jerusalemdeclaration.org/#jda)

1. A. General (YES Codes)

   1.1 A1
   - A1ESSENTIAL
     "It is racist to essentialize (treat a character trait as inherent) or to make sweeping negative generalizations about a given population."

   1.2 A2
   - A2EVIL
     "Jews are linked to the forces of evil."
   - A2CONSPIRACY
     "the idea of a Jewish conspiracy"
   - A2HIDDEN
     "\"the Jews\" possess hidden power"
   - A2COLLECTIVEAGENDA
     "promote their own collective agenda at the expense of other people."
   - A2CONTROLGOV
     "\"the Jews\" control governments with a \"hidden hand\""
   - A2CONTROLBANKS
     "own the banks"
   - A2CONTROLMEDIA
     "control the media"
   - A2FIFTHCOLUMN
     "act as \"a state within a state\""
   - A2DISEASE
     "responsible for spreading disease (such as Covid-19)."

   1.3 A3
   - A3WEALTH
     "all Jews are wealthy"
   - A3STINGY
     "inherently stingy"
   - A3UNPATRIOTIC
     "or unpatriotic."
   - A3CARICATURE
     "depicted as grotesque, with big noses and associated with wealth."
   - A3ASSAULT
     "assaulting someone because she or he is Jewish"
   - A3SYNAGOGUE
     "attacking a synagogue"
   - A3SWASTIKA
     "daubing swastikas on Jewish graves"
   - A3EMPLOYMENT
     "refusing to hire or promote people because they are Jewish."

   1.4 A4
   - A4DOGWHISTLE
     "Antisemitism can be direct or indirect, explicit or coded."
   - A4ROTHSCHILD
     "\"the Rothschilds control the world\""
   - A4ISRAELEVIL
     "portraying Israel as the ultimate evil"
   - A4ISRAELINFLUENCE
     "grossly exaggerating its actual influence"

   1.5 A5
   - A5HOLOCAUSTDENIAL
     "Denying or minimizing the Holocaust by claiming that the deliberate Nazi genocide of the Jews did not take place"
   - A5HOLOCAUSTMECHANISM
     "there were no extermination camps or gas chambers"
   - A5HOLOCAUSTMINIMIZE
     "the number of victims was a fraction of the actual total"

2. B. Israel and Palestine: examples that, on the face of it, are antisemitic (YES Codes)

   2.1 B6
   - B6ISRAELCARICATURE
     "Applying the symbols, images and negative stereotypes of classical antisemitism... to the State of Israel."

   2.2 B7
   - B7COLLECTIVEBLAME
     "Holding Jews collectively responsible for Israel’s conduct"
   - B7ISRAELAGENT
     "treating Jews, simply because they are Jewish, as agents of Israel."

   2.3 B8
   - B8FORCECONDEMN
     "Requiring people, because they are Jewish, publicly to condemn Israel or Zionism"

   2.4 B9
   - B9ISRAELFIFTHCOLUMN
     "Assuming that non-Israeli Jews, simply because they are Jews, are necessarily more loyal to Israel than to their own countries."

   2.5 B10
   - B10JEWISHRIGHTS
     "Denying the right of Jews in the State of Israel to exist and flourish, collectively and individually, as Jews, in accordance with the principle of equality."

3. C. Israel and Palestine: examples that, on the face of it, are not antisemitic (NO Codes)

   3.1 C11
   - C11PALESTINIANJUSTICE
     "Supporting the Palestinian demand for justice"
   - C11PALESTINIANRIGHTS
     "the full grant of their political, national, civil, and human rights, as encapsulated in international law."

   3.2 C12
   - C12ZIONCRITICAL
     "Criticizing or opposing Zionism as a form of nationalism"
   - C12SOLUTIONS
     "arguing for a variety of constitutional arrangements for Jews and Palestinians... whether in two states, a binational state, unitary democratic state, federal state, or in whatever form."
   - C12EQUALRIGHTS
     "support arrangements that accord full equality to all inhabitants \"between the river and the sea\""

   3.3 C13
   - C13ISRAELEVIDENCE
     "Evidence-based criticism of Israel as a state."
   - C13ISRAELINSTITUTIONS
     "its institutions and founding principles."
   - C13ISRAELPOLICIES
     "its policies and practices, domestic and abroad"
   - C13ISRAELOPT
     "the conduct of Israel in the West Bank and Gaza"
   - C13ISRAELREGION
     "the role Israel plays in the region"
   - C13ISRAELDISCRIMINATION
     "It is not antisemitic to point out systematic racial discrimination."
   - C13ISRAELNORMS
     "the same norms of debate that apply to other states"
   - C13ISRAELCOMPARE
     "to compare Israel with other historical cases, including settler-colonialism or apartheid."

   3.4 C14
   - C14BDS
     "Boycott, divestment and sanctions are commonplace, non-violent forms of political protest against states. In the Israeli case they are not, in and of themselves, antisemitic."

   3.5 C15
   - C15REASONABLE
     "Political speech does not have to be measured, proportional, tempered, or reasonable... the line between antisemitic and non-antisemitic speech is different from the line between unreasonable and reasonable speech.""
   - C15DOUBLESTANDARD
     "Criticism that some may see as excessive or contentious, or as reflecting a \"double standard\", is not, in and of itself, antisemitic."

4. NOOTHER_J: Text is not antisemitic and does not fit the JDA definition.

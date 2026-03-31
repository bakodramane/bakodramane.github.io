---
layout: post
title: "Weekly update on AI tools for surveys and administrative data: notable surge of activity at the intersection of Artificial Intelligence and survey research"
date: 2026-03-13
categories: [AI, Survey Research, Weekly Update]
tags: [AI, surveys, statistics, official-statistics, bilingual]
lang: en
---

## 🇬🇧 English

This article is part of weekly updates on new developments in the use of AI methods and tools of surveys (households, individuals, farms…) and administrative data for official statistics

Prepared by: Dramane Bako, Statistician/Data scientist (FAO Statistics Division, Rome, Italy)

Coverage Period: 09–15 March 2026

Key words: AI, survey research, official statistics, machine learning, data quality, household surveys, data analysis

Executive Summary

The past week has brought a notable surge of activity at the intersection of Artificial Intelligence and survey research. Flagship publications from the IMF, Eurostat, and India's Ministry of Statistics, alongside peer-reviewed studies on LLM-based imputation and survey bot detection, collectively signal that the field is moving from exploratory experimentation to operational deployment. At the same time, the 57th UN Statistical Commission and the UNECE Expert Meeting on Ethics in Official Statistics have placed governance, trust, and responsible AI firmly at the centre of institutional agendas. This report organises the week's key developments across the full survey data lifecycle.

1. Survey Design and Questionnaire Development

1.1 AI-Assisted Instrument Design

Generative AI tools are increasingly being used to draft, adapt, and pre-test survey questionnaires. Researchers at Unisanté presented a roadmap for AI-assisted surveys at a colloquium in early March 2026, arguing that AI tools can now be applied at every stage of the survey research process—from literature review and study design to questionnaire pre-testing, data collection, and analysis [1]. The roadmap identifies adaptive questioning, where AI dynamically adjusts question routing based on prior responses, as a particularly high-value application for Computer-Assisted Personal Interviewing (CAPI) and Computer-Assisted Telephone Interviewing (CATI) systems.

Separately, a study published in the Journal of Medical Internet Research examined AI in medical questionnaire development, finding that AI substantially accelerates the instrument development cycle while maintaining psychometric validity, provided that human expert review is retained as a final validation step [2].

1.2 The AI Bot Contamination Problem

One of the most pressing methodological challenges of the current period is the contamination of online survey panels by AI-generated responses. A correspondence published in Nature in March 2026 reports that an AI-based reasoning tool was used to build a bot that, in 6,700 tests, passed standard attention-check questions with a 99.8% success rate [3]. The authors argue that this development does not create a new data quality problem but rather makes an existing one—careless or fraudulent human respondents—impossible to ignore.

A separate study published in the International Journal of Social Research Methodology investigated a real-world bot attack on an educational survey, documenting the data cleaning protocols required to filter bot-automated responses and recommending a multifaceted approach combining behavioural paradata, timing analysis, and identity verification [4]. Meanwhile, a framework published in the Journal of Consumer Research suggests that the actual AI contamination rate on platforms with robust identity verification (such as Prolific) may currently be near zero, indicating that platform-level controls can be effective [5].

The implications for household surveys conducted via web panels are significant. Statistical offices relying on web-based data collection should consider the following mitigation strategies:

2. Data Editing and Cleaning

2.1 LLMs for Missing Data Imputation: A Large-Scale Benchmark

A landmark benchmarking study submitted to arXiv on 20 March 2026 provides the most comprehensive evaluation to date of LLMs for missing data imputation in tabular datasets [6]. The study, conducted by Mangussi et al., compared five widely used LLMs against six state-of-the-art imputation baselines across 29 datasets under three standard missingness mechanisms: Missing Completely at Random (MCAR), Missing at Random (MAR), and Missing Not at Random (MNAR), with missing rates of up to 20%.

The principal findings are as follows. On real-world open-source datasets, leading LLMs—particularly Gemini 3.0 Flash and Claude 4.5 Sonnet—consistently outperformed traditional methods. However, on synthetic datasets, traditional methods such as MICE (Multiple Imputation by Chained Equations) retained their superiority. The study concludes that LLM effectiveness in imputation is driven by semantic context and domain-specific knowledge absorbed during pre-training, rather than purely statistical reconstruction. This means LLMs are most valuable when the missingness pattern is related to the substantive meaning of the variables—a common situation in household surveys covering income, health, and employment [6].

A critical trade-off is identified: while LLMs excel in imputation quality on real-world data, they incur significantly higher computational time and monetary costs compared to classical methods. For statistical offices processing large-scale household surveys, this cost-quality trade-off requires careful evaluation.

"LLMs are promising semantics-driven imputers for complex tabular data, but their advantage is closely tied to the models' prior exposure to domain-specific patterns learned during pre-training on internet-scale corpora."

— Mangussi et al. (2026) [6]

A complementary study on in-context learning for survey data imputation, presented at a workshop bridging NLP and survey statistics, demonstrated that LLMs can be used for multiple imputation—generating several plausible imputed values to properly account for the uncertainty associated with missing data—a key requirement for valid statistical inference [7].

2.2 Automated Coding of Open-Ended Responses

The manual coding of open-ended survey responses has long been a bottleneck in survey processing. AI-native platforms using NLP are now capable of identifying themes, scoring sentiment, and correlating qualitative findings with quantitative variables across thousands of responses in seconds. Industry analyses suggest that AI can reduce the open-ended response coding cycle from five to seven weeks to a matter of hours [8]. For national statistical offices that include open-ended questions in household surveys—such as questions on subjective well-being, reasons for non-participation in the labour market, or barriers to healthcare access—this represents a transformative efficiency gain.

3. Data Processing and Statistical Analysis

3.1 Evaluating LLMs on Complex Survey Microdata

The question of whether AI tools can generate statistically defensible results from complex survey microdata was addressed directly by Mathematica in a study published on 18 March 2026 [9]. Using the American Community Survey Public Use Microdata Sample, the team constructed 35 validated analytic tasks spanning weighted population estimates and causal inference methods, then compared model outputs to validated benchmark estimates under two conditions: reasoning only (no data access) and code-execution enabled.

The results are instructive for any organisation considering AI-assisted survey analysis:

Code execution is foundational. Under reasoning-only conditions, error rates were substantial—often large enough to change the conclusions a decision-maker would draw. With code execution enabled, accuracy increased dramatically.

Statistical competence varies across models. On descriptive tasks, model accuracy ranged from 75% to 92%. On causal inference tasks, the spread was even wider.

Data governance amplifies model performance. Poorly labelled variables, ambiguous metadata, and weak documentation degraded performance across all models. The study warns that "AI systems do not overcome weak data governance—they amplify it" [9].

These findings carry direct implications for statistical offices: embedding LLMs in tool-enabled, code-executing workflows is a prerequisite for trustworthy AI-assisted analysis, and investment in data documentation and metadata standards is as important as model selection.

3.2 Small Area Estimation in the Era of Machine Learning

A review article published in the Journal of Official Statistics in 2025 and receiving renewed attention in March 2026 addresses the growing use of machine learning for small area estimation (SAE)—a critical application for household surveys that must produce subnational estimates [10]. The article, by Tzavidis, documents the rapid proliferation of ML-based SAE approaches, including Meta's methodology for producing global wealth estimates at 2.4 km² resolution using household survey data combined with remote sensing, mobile phone data, and social connectivity data.

The review identifies three key methodological challenges that statistical offices must address when adopting ML for SAE:

Uncertainty quantification: Many ML-based SAE approaches do not adequately account for sampling error in the survey-based ground truth data, nor do they provide reliable uncertainty estimates for the resulting small area estimates.

Model specification and overfitting: The automatic model selection capabilities of ML algorithms can lead to overfitting, particularly when training data are sparse at the area level.

Integration of alternative data sources: The use of non-traditional data (satellite imagery, administrative records, mobile data) as predictors requires careful validation to ensure that the relationships observed in training data generalise to out-of-sample areas [10].

4. Reporting and Dissemination

4.1 IMF StatGPT: Making Official Statistics AI-Ready

The most significant institutional publication of the week is the IMF's Departmental Paper on StatGPT, released on 10 March 2026 [11]. The paper addresses a fundamental problem: while LLMs and generative AI applications such as ChatGPT and Gemini appear to offer a natural language interface to official statistics, testing demonstrates that they frequently provide "dangerously reasonable" but incorrect figures.

StatGPT's solution is architecturally elegant: instead of relying on the LLM to generate statistics from its internal weights, it uses the LLM to generate structured queries against the APIs of official statistical agencies. The result is that users receive the exact published figures every time, while benefiting from natural language interaction. The paper also proposes a roadmap for making official statistics AI-ready through three pillars:

4.2 India's AI-Driven Statistical Ecosystem

India's Ministry of Statistics and Programme Implementation (MoSPI) announced a comprehensive AI transformation of its statistical infrastructure on 20 March 2026 [12]. The initiative encompasses several interconnected developments:

e-Sankhyiki and Model Context Protocol (MCP): In February 2026, the National Statistics Office launched a beta version of an MCP server on the e-Sankhyiki portal—India's national platform for official statistics, which hosts 21 statistical products with over 136 million records. The MCP server enables users to connect their own AI agents directly to official datasets, query data without downloading large files, and automate statistical reporting through a unified interface.

Semantic Search and AI Chatbots: A beta version of semantic search allows users to explore datasets through natural language prompts. An AI-powered chatbot on the MoSPI website provides context-based responses to queries about datasets, reports, and publications.

BharatGen: India's sovereign multilingual LLM, launched in June 2025, supports 22 Indian languages and underpins several of these AI-enabled statistical access systems [12].

4.3 Eurostat 2026 AI Report

Eurostat released its 2026 edition of "The Use of Artificial Intelligence Technologies in the European Union" this week, based on the 2025 ICT Household Survey and Enterprise Survey [13]. Key findings include:

20.0% of all EU enterprises used at least one AI technology in 2025, up from previous years.

44.0% of large enterprises used at least two AI technologies, compared to 10.6% of small enterprises.

The information and communication sector leads adoption at 62.5%, followed by professional, scientific, and technical services at 40.4%.

The 2025 ICT Household Survey introduced AI-specific questions for the first time, focusing on the conscious use of generative AI (e.g., ChatGPT, Copilot, Gemini) to create content in the past three months [13].

5. Governance, Ethics, and Institutional Developments

5.1 UNECE Expert Meeting on Ethics in Official Statistics (March 2026)

The UNECE convened an Expert Meeting on Ethics in Official Statistics in Geneva on 12–13 March 2026, bringing together senior managers and communication professionals from national statistical offices worldwide [14]. The meeting addressed the ethical dimensions of AI adoption in official statistics across four thematic sessions:

Defining ethics in official statistics: Eurostat presented its Data Ethics Principles for European Official Statistics, emphasising transparency, accountability, and the alignment of AI use with the EU AI Act.

Ethical dilemmas for NSOs: Presentations from Statistics Indonesia, Kenya National Bureau of Statistics, and Statistics Canada highlighted the challenges of multi-source statistics, citizen-generated data, and digital sovereignty.

Ethics in AI for dissemination: A dedicated presentation examined the ethical considerations in using AI for the dissemination and communication of statistics, including the risks of automated narrative generation and the need for human oversight.

Public trust: The meeting concluded that public trust is a vital institutional asset that must be actively protected through clear ethical standards and transparent communication about AI use [14].

5.2 57th UN Statistical Commission: AI as the Defining Theme

The 57th Session of the UN Statistical Commission, held in New York from 3–6 March 2026, was described by observers as having AI as its defining theme. Delegates tackled questions around AI readiness, threats to core statistical processes, and the modernisation of official statistics. A high-level side event on "AI-Readiness for Official Data and Statistics" emphasised that the objective of AI readiness is to ensure users receive accurate, timely, coherent, and contextually relevant data with clear provenance [15]. Saudi Arabia's General Authority for Statistics reported on its integration of AI and Geo-AI technologies into statistical operations as part of its digital transformation strategy.

6. Key Resources and Tools

7. Implications and Outlook

The developments of this week collectively point to several strategic priorities for researchers and statistical offices:

Invest in AI-ready data infrastructure. The IMF's StatGPT paper and India's e-Sankhyiki MCP integration both demonstrate that the value of AI in statistical dissemination depends critically on the availability of machine-readable APIs and enriched metadata. Statistical offices that have not yet adopted open data standards will be at a growing disadvantage.

Adopt tool-enabled AI workflows for analysis. Mathematica's evaluation framework provides compelling evidence that LLMs must be embedded in code-executing, tool-enabled workflows to be reliable for statistical analysis. Stand-alone chat-based AI should not be used for policy-relevant survey analysis without rigorous validation.

Treat LLM imputation as a complement, not a replacement. The benchmark study by Mangussi et al. shows that LLMs can outperform traditional methods on real-world survey data, but their advantages are domain-specific and come with higher costs. A hybrid approach—using LLMs for semantically complex variables and traditional methods for synthetic or structurally simple data—is likely optimal.

Strengthen survey quality controls for the AI age. The near-perfect performance of AI bots on attention checks demands a fundamental rethink of online survey quality assurance. Platform-level identity verification, behavioural paradata analysis, and structural survey design changes are the most effective countermeasures.

Engage with ethical and governance frameworks proactively. The UNECE meeting and the EU AI Act signal that the regulatory environment for AI in official statistics is crystallising rapidly. Statistical offices should engage with these frameworks now, establishing internal AI ethics guidelines and governance structures before deployment rather than after.

References

[1] Callegaro Research. (2026, March 7). Colloquium: A roadmap to AI assisted surveys. Unisanté. Retrieved from https://callegaroresearch.com/2026/03/07/colloquium-a-roadmap-to-ai-assisted-surveys/

[2] Ji, J., Kim, J., & Kim, Y. (2024). Predicting missing values in survey data using prompt engineering for addressing item non-response. Future Internet, 16(10), 351. Retrieved from https://www.mdpi.com/1999-5903/16/10/351

[3] Wang, M. D., & Su, X. (2026). Rethinking AI's role in survey research: from threat to collaboration. Nature, 651, 846. https://doi.org/10.1038/d41586-026-00862-9

[4] Tandfonline. (2026). Online survey data integrity: lessons learnt from investigating a bot attack on a small-scale educational study. International Journal of Social Research Methodology. https://doi.org/10.1080/13645579.2026.2636205

[5] Affonso, F. M., et al. (2026). A Framework for Detecting AI Agents in Online Research. Journal of Consumer Research. https://doi.org/10.1093/jcr/ucag006

[6] Mangussi, A. D., Pereira, R. C., Lorena, A. C., & Abreu, P. H. (2026). Large Language Models for Missing Data Imputation: Understanding Behavior, Hallucination Effects, and Control Mechanisms. arXiv:2603.22332. Retrieved from https://arxiv.org/abs/2603.22332

[7] Holtdirk, T., Ahnert, G., & Haensch, A. C. (2026). In-Context Learning for the Imputation of Survey Data. First Workshop on Bridging NLP and Survey Statistics. Retrieved from https://openreview.net/forum?id=9uABaUyZne

[8] Sopact. (2026). Analyze Open-Ended Survey Response. Retrieved from https://www.sopact.com/use-case/analyze-open-ended-survey

[9] Nigenda, A., Dotter, D., & Burns, M. (2026, March 18). Trusting your LLM: AI's handling of complex statistical data. Mathematica. Retrieved from https://www.mathematica.org/blogs/trusting-your-llm

[10] Tzavidis, N. (2025). Small Area Estimation in the Era of Machine Learning and Alternative Data Sources: Opportunities, Challenges, and Outlook. Journal of Official Statistics, 41(3). https://doi.org/10.1177/0282423X251342004

[11] Tebrake, J., Boukherouaa, E. B., Danforth, J., & Harikrishnan, N. (2026). StatGPT: AI for Official Statistics. IMF Departmental Paper No. 2026/004. Retrieved from https://www.imf.org/en/publications/departmental-papers-policy-papers/issues/2026/03/10/statgpt-ai-for-official-statistics-573514

[12] Press Information Bureau, Government of India. (2026, March 20). AI-Driven Transformation of India's Statistical and Data Ecosystem. Retrieved from https://www.pib.gov.in/PressNoteDetails.aspx?id=157886&NoteId=157886&ModuleId=3&reg=3&lang=1

[13] Eurostat. (2026). The Use of Artificial Intelligence (AI) Technologies in the European Union: Key Results, 2026 Edition. Retrieved from https://ec.europa.eu/eurostat/documents/7870049/23260410/KS-01-26-009-EN-N.pdf

[14] UNECE. (2026). Expert Meeting on Ethics in Official Statistics. Geneva, 12–13 March 2026. Retrieved from https://unece.org/statistics/events/Ethics2026

[15] UN Statistical Commission. (2026). High Level Side Event: AI-Readiness for Official Data & Statistics at the 57th Session of the UN Statistical Commission. Retrieved from https://www.instagram.com/p/DVdLFb0AamB/

This report is intended as a weekly digest for researchers and statistical professionals. Readers are encouraged to consult the original sources for full methodological details. Feedback and suggestions for coverage in future editions are welcome.

Contact: bakodramane@gmail.com

---

## 🇫🇷 Français

**Mise à jour hebdomadaire sur les outils d'IA pour les enquêtes et les données administratives : une recrudescence notable d'activités à l'intersection de l'intelligence artificielle et de la recherche par sondage**

Cet article fait partie des mises à jour hebdomadaires sur les nouveaux développements dans l'utilisation des méthodes et outils d'IA pour les enquêtes (ménages, individus, exploitations agricoles…) et les données administratives pour les statistiques officielles.

Préparé par : Dramane Bako, Statisticien/Scientifique des données (Division des statistiques de la FAO, Rome, Italie)

Période couverte : 09–15 mars 2026

Mots-clés : IA, recherche par sondage, statistiques officielles, apprentissage automatique, qualité des données, enquêtes auprès des ménages, analyse de données

Résumé

La semaine dernière a été marquée par une recrudescence notable d'activités à l'intersection de l'intelligence artificielle et de la recherche par sondage. Des publications phares du FMI, d'Eurostat et du ministère indien des Statistiques, ainsi que des études évaluées par des pairs sur l'imputation basée sur les LLM et la détection de robots d'enquête, signalent collectivement que le domaine passe de l'expérimentation exploratoire au déploiement opérationnel. Parallèlement, la 57e Commission de statistique des Nations Unies et la Réunion d'experts de la CEE-ONU sur l'éthique dans les statistiques officielles ont placé la gouvernance, la confiance et l'IA responsable fermement au centre des agendas institutionnels. Ce rapport organise les développements clés de la semaine à travers le cycle de vie complet des données d'enquête.

1. Conception d'enquêtes et élaboration de questionnaires

1.1 Conception d'instruments assistée par l'IA

Les outils d'IA générative sont de plus en plus utilisés pour rédiger, adapter et pré-tester les questionnaires d'enquête. Des chercheurs d'Unisanté ont présenté une feuille de route pour les enquêtes assistées par l'IA lors d'un colloque début mars 2026, arguant que les outils d'IA peuvent désormais être appliqués à chaque étape du processus de recherche par sondage – de la revue de la littérature et de la conception de l'étude au pré-test du questionnaire, à la collecte et à l'analyse des données [1]. La feuille de route identifie l'interrogation adaptative, où l'IA ajuste dynamiquement le routage des questions en fonction des réponses précédentes, comme une application particulièrement précieuse pour les systèmes d'entretien personnel assisté par ordinateur (CAPI) et d'entretien téléphonique assisté par ordinateur (CATI).

Séparément, une étude publiée dans le Journal of Medical Internet Research a examiné l'IA dans le développement de questionnaires médicaux, constatant que l'IA accélère considérablement le cycle de développement des instruments tout en maintenant la validité psychométrique, à condition que l'examen par des experts humains soit conservé comme étape de validation finale [2].

1.2 Le problème de la contamination par les robots d'IA

L'un des défis méthodologiques les plus pressants de la période actuelle est la contamination des panels d'enquêtes en ligne par des réponses générées par l'IA. Une correspondance publiée dans Nature en mars 2026 rapporte qu'un outil de raisonnement basé sur l'IA a été utilisé pour construire un robot qui, en 6 700 tests, a réussi les questions de vérification d'attention standard avec un taux de réussite de 99,8 % [3]. Les auteurs soutiennent que ce développement ne crée pas un nouveau problème de qualité des données, mais rend plutôt impossible d'ignorer un problème existant – celui des répondants humains négligents ou frauduleux.

Une étude distincte publiée dans l'International Journal of Social Research Methodology a examiné une attaque de robot réelle sur une enquête éducative, documentant les protocoles de nettoyage des données nécessaires pour filtrer les réponses automatisées par des robots et recommandant une approche multifacette combinant des paradata comportementales, une analyse temporelle et une vérification d'identité [4]. Parallèlement, un cadre publié dans le Journal of Consumer Research suggère que le taux réel de contamination par l'IA sur les plateformes dotées d'une vérification d'identité robuste (telles que Prolific) pourrait actuellement être proche de zéro, ce qui indique que les contrôles au niveau de la plateforme peuvent être efficaces [5].

Les implications pour les enquêtes auprès des ménages menées via des panels web sont importantes. Les offices statistiques qui s'appuient sur la collecte de données via le web devraient envisager les stratégies d'atténuation suivantes :

2. Édition et nettoyage des données

2.1 LLM pour l'imputation des données manquantes : une évaluation à grande échelle

Une étude comparative historique soumise à arXiv le 20 mars 2026 fournit l'évaluation la plus complète à ce jour des LLM pour l'imputation des données manquantes dans les ensembles de données tabulaires [6]. L'étude, menée par Mangussi et al., a comparé cinq LLM largement utilisés à six références d'imputation de pointe sur 29 ensembles de données selon trois mécanismes de données manquantes standard : Missing Completely at Random (MCAR), Missing at Random (MAR) et Missing Not at Random (MNAR), avec des taux de données manquantes allant jusqu'à 20 %.

Les principales conclusions sont les suivantes. Sur des ensembles de données open source réels, les LLM de premier plan – en particulier Gemini 3.0 Flash et Claude 4.5 Sonnet – ont constamment surpassé les méthodes traditionnelles. Cependant, sur des ensembles de données synthétiques, les méthodes traditionnelles telles que MICE (Multiple Imputation by Chained Equations) ont conservé leur supériorité. L'étude conclut que l'efficacité des LLM en matière d'imputation estTirée du contexte sémantique et des connaissances spécifiques au domaine absorbées lors du pré-entraînement, plutôt que d'une reconstruction purement statistique. Cela signifie que les LLM sont plus précieux lorsque le modèle de données manquantes est lié à la signification substantielle des variables – une situation courante dans les enquêtes auprès des ménages couvrant le revenu, la santé et l'emploi [6].

Un compromis critique est identifié : si les LLM excellent en qualité d'imputation sur les données réelles, ils entraînent des temps de calcul et des coûts monétaires nettement plus élevés que les méthodes classiques. Pour les offices statistiques traitant des enquêtes auprès des ménages à grande échelle, ce compromis coût-qualité nécessite une évaluation minutieuse.

« Les LLM sont des imputeurs prometteurs basés sur la sémantique pour les données tabulaires complexes, mais leur avantage est étroitement lié à l'exposition préalable des modèles à des modèles spécifiques au domaine appris lors du pré-entraînement sur des corpus à l'échelle d'Internet. »

— Mangussi et al. (2026) [6]

Une étude complémentaire sur l'apprentissage en contexte pour l'imputation de données d'enquête, présentée lors d'un atelier reliant le traitement du langage naturel et les statistiques d'enquête, a démontré que les LLM peuvent être utilisés pour l'imputation multiple – générant plusieurs valeurs imputées plausibles pour tenir compte correctement de l'incertitude associée aux données manquantes – une exigence clé pour une inférence statistique valide [7].

2.2 Codage automatisé des réponses ouvertes

Le codage manuel des réponses ouvertes aux enquêtes a longtemps été un goulot d'étranglement dans le traitement des enquêtes. Les plateformes natives d'IA utilisant le traitement du langage naturel sont désormais capables d'identifier des thèmes, d'évaluer le sentiment et de corréler des résultats qualitatifs avec des variables quantitatives sur des milliers de réponses en quelques secondes. Les analyses de l'industrie suggèrent que l'IA peut réduire le cycle de codage des réponses ouvertes de cinq à sept semaines à quelques heures [8]. Pour les offices statistiques nationaux qui incluent des questions ouvertes dans les enquêtes auprès des ménages – telles que des questions sur le bien-être subjectif, les raisons de la non-participation au marché du travail ou les obstacles à l'accès aux soins de santé – cela représente un gain d'efficacité transformateur.

3. Traitement des données et analyse statistique

3.1 Évaluation des LLM sur des microdonnées d'enquête complexes

La question de savoir si les outils d'IA peuvent générer des résultats statistiquement défendables à partir de microdonnées d'enquête complexes a été directement abordée par Mathematica dans une étude publiée le 18 mars 2026 [9]. En utilisant l'échantillon de microdonnées à usage public de l'American Community Survey, l'équipe a construit 35 tâches analytiques validées couvrant des estimations de population pondérées et des méthodes d'inférence causale, puis a comparé les résultats du modèle à des estimations de référence validées dans deux conditions : raisonnement uniquement (pas d'accès aux données) et exécution de code activée.

Les résultats sont instructifs pour toute organisation envisageant une analyse d'enquête assistée par l'IA :

L'exécution de code est fondamentale. Dans les conditions de raisonnement uniquement, les taux

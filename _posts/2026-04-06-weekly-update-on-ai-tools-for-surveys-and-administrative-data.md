# Weekly update on AI tools for surveys and administrative data: AI adoption, LLM evaluation, and StatGPT

Date: 2026-04-06



## 🇬🇧 English

This article is part of weekly updates on new developments in the use of AI methods and tools of surveys (households, individuals, farms…) and administrative data for official statistics

Prepared by: Dramane Bako, Statistician/Data scientist (FAO Statistics Division, Rome, Italy)

Coverage Period: 30 March – 5 April 2026

Key words: AI, survey research, official statistics, machine learning, data quality, household surveys, statistical methods, data analysis

Key Takeaways

AI adoption in the US economy is growing rapidly: Business survey data from the Census Bureau show that about 18 percent of firms have adopted AI as of year-end 2025, with significant variation across firm size and industry cohorts.

Generative AI is transforming survey design but requires human oversight: While AI tools can accelerate survey writing and generate strong drafts, they often underestimate respondent burden and produce flawed response options, necessitating expert review.

Evaluating LLMs on complex statistical data is crucial: Organizations must implement structured evaluation frameworks to test LLM performance in tool-enabled, multistep analytic workflows, as stand-alone reasoning is insufficient for applied statistical work.

The IMF introduces StatGPT for official statistics: StatGPT leverages LLMs to generate structured queries against APIs of official statistical agencies, ensuring users receive exact published figures while benefiting from natural language interaction.

1. Data Editing & Error Detection

2. Data Cleaning & Imputation

3. Natural Language Processing & LLMs for Survey Design

Generative AI chatbots are increasingly used by UX researchers to quickly deploy surveys. When given a clear research objective and prompted to use survey-design best practices, tools like ChatGPT and Claude can generate a solid first draft in seconds [1]. However, these tools often underestimate respondent burden and can produce flawed response options, such as omitting an "Other" option or generating semantically unbalanced rating scales [1]. Therefore, human expertise remains essential for oversight and pilot testing with real people is crucial to reveal confusion or friction that AI cannot detect [1].

4. AI for Survey Data Processing, Coding, and Classification

5. Machine Learning & AI for Survey Data Analysis, Weighting, and Estimation

As organizations integrate large language models (LLMs) into analytic workflows, evaluating their performance on complex statistical data is critical. A recent evaluation framework tested LLM performance in tool-enabled, multistep analytic workflows using complex survey data [2]. The findings revealed that code execution is foundational; when limited to reasoning alone, error rates were substantial, but accuracy increased significantly when models could access data and execute code [2]. Furthermore, statistical competence varies meaningfully across models, especially for causal inference tasks, highlighting the need for structured evaluation frameworks grounded in real data and controlled tool use [2].

6. AI in Survey Reporting, Data Visualization, and Dissemination

7. AI in Survey Methodology

8. AI in Official Statistics and Household Surveys

The adoption of AI in the US economy is being closely monitored through various surveys. Business survey data from the Census Bureau indicate that about 18 percent of firms have adopted AI as of year-end 2025 [3]. The Real-Time Population Survey reports that work-related Generative AI adoption stands at about 41 percent as of November 2025 [3]. These surveys also reveal considerable heterogeneity across firm size and industry cohorts, with robust adoption in high-value services sectors suggesting that current AI usage is most prevalent in cognitive and analytical work [3].

In the realm of official statistics, the IMF has introduced StatGPT, an initiative that leverages LLMs to generate structured queries against APIs of official statistical agencies [4]. This approach ensures that users receive the exact published figures while benefiting from natural language interaction, overcoming the limitations of off-the-shelf GenAI applications that frequently provide incorrect figures [4].

Additionally, the Committee on National Statistics, the Federal Committee on Statistical Methodology, and the National Institute of Statistical Sciences are organizing a second AI Day for Federal Statistics on April 30, 2026 [5]. This workshop will explore the implications of AI for federal statistics, providing opportunities for training, capacity building, and sharing best practices for using AI to drive government efficiency and modernize the federal workforce [5].

References

[1] AI Can Help with Survey Writing, But It Still Requires Human Expertise. Nielsen Norman Group. https://www.nngroup.com/articles/ai-survey-writing/

[2] Trusting your LLM: AI’s handling of complex statistical data. Mathematica. https://www.mathematica.org/blogs/trusting-your-llm

[3] Monitoring AI Adoption in the US Economy. Federal Reserve. https://www.federalreserve.gov/econres/notes/feds-notes/monitoring-ai-adoption-in-the-u-s-economy-20260403.html

[4] StatGPT: AI for Official Statistics. International Monetary Fund. https://www.imf.org/en/publications/departmental-papers-policy-papers/issues/2026/03/10/statgpt-ai-for-official-statistics-573514

[5] AI Day for Federal Statistics 2026. Population Association of America. https://www.populationassociation.org/events/event-description?CalendarEventKey=f26dfb08-99f4-42fa-921a-019cb515a57b&Home=%2Fhome

Contact: bakodramane@gmail.com

---

## 🇫🇷 Français

**Mise à jour hebdomadaire sur les outils d'IA pour les enquêtes et les données administratives : adoption de l'IA, évaluation des LLM et StatGPT**

Cet article fait partie des mises à jour hebdomadaires sur les nouvelles avancées dans l’utilisation des méthodes et outils d’IA pour les enquêtes (ménages, individus, exploitations agricoles…) et les données administratives destinées aux statistiques officielles.

Préparé par : Dramane Bako, Statisticien/Data scientist (FAO Statistics Division, Rome, Italie)

Période couverte : 30 mars – 5 avril 2026

Mots-clés : IA, recherche par sondage, statistiques officielles, apprentissage automatique, qualité des données, enquêtes ménages, méthodes statistiques, analyse de données

Points clés à retenir

L’adoption de l’IA dans l’économie américaine croît rapidement : Les données d’enquêtes auprès des entreprises du Census Bureau montrent qu’environ 18 % des entreprises ont adopté l’IA fin 2025, avec des variations significatives selon la taille et le secteur d’activité.

L’IA générative transforme la conception des enquêtes mais nécessite une supervision humaine : Bien que les outils d’IA puissent accélérer la rédaction des enquêtes et produire des brouillons solides, ils sous-estiment souvent la charge imposée aux répondants et génèrent des options de réponse erronées, rendant indispensable une revue experte.

Il est crucial d’évaluer les LLMs sur des données statistiques complexes : Les organisations doivent mettre en œuvre des cadres d’évaluation structurés pour tester les performances des LLM dans des workflows analytiques multietapes assistés par outils, car le raisonnement autonome est insuffisant pour les travaux statistiques appliqués.

Le FMI introduit StatGPT pour les statistiques officielles : StatGPT exploite les LLM pour générer des requêtes structurées via les API des agences statistiques officielles, garantissant aux utilisateurs l’accès aux chiffres publiés exacts tout en bénéficiant de l’interaction en langage naturel.

1. Édition des données et détection des erreurs

2. Nettoyage des données et imputation

3. Traitement du langage naturel et LLM pour la conception des enquêtes

Les chatbots d’IA générative sont de plus en plus utilisés par les chercheurs UX pour déployer rapidement des enquêtes. Lorsqu’on leur fournit un objectif de recherche clair et les meilleures pratiques de conception d’enquête, des outils comme ChatGPT et Claude peuvent générer un premier brouillon solide en quelques secondes [1]. Cependant, ces outils sous-estiment souvent la charge du répondant et peuvent produire des options de réponse défectueuses, telles que l’omission de l’option « Autre » ou la création d’échelles de notation sémantiquement déséquilibrées [1]. Par conséquent, l’expertise humaine reste essentielle pour la supervision, et les tests pilotes avec des personnes réelles sont cruciaux pour révéler des confusions ou des frictions indétectables par l’IA [1].

4. IA pour le traitement, le codage et la classification des données d’enquête

5. Apprentissage automatique et IA pour l’analyse, le pondération et l’estimation des données d’enquête

À mesure que les organisations intègrent les grands modèles de langage (LLM) dans leurs workflows analytiques, il est essentiel d’évaluer leurs performances sur des données statistiques complexes. Un cadre d’évaluation récent a testé les performances des LLM dans des workflows analytiques multietapes assistés par outils utilisant des données d’enquête complexes [2]. Les résultats ont montré que l’exécution de code est fondamentale ; lorsqu’ils se limitent au seul raisonnement, les taux d’erreur sont élevés, mais la précision augmente considérablement lorsque les modèles peuvent accéder aux données et exécuter du code [2]. De plus, la compétence statistique varie significativement selon les modèles, en particulier pour les tâches d’inférence causale, ce qui souligne la nécessité de cadres d’évaluation structurés basés sur des données réelles et un usage contrôlé des outils [2].

6. IA dans le reporting, la visualisation et la diffusion des enquêtes

7. IA en méthodologie d’enquête

8. IA dans les statistiques officielles et les enquêtes ménages

L’adoption de l’IA dans l’économie américaine est étroitement suivie via diverses enquêtes. Les données d’enquêtes auprès des entreprises du Census Bureau indiquent qu’environ 18 % des entreprises ont adopté l’IA fin 2025 [3]. L’enquête Real-Time Population Survey rapporte que l’adoption de l’IA générative liée au travail atteint environ 41 % en novembre 2025 [3]. Ces enquêtes révèlent également une hétérogénéité considérable selon la taille des entreprises et les secteurs, avec une adoption robuste dans les secteurs des services à forte valeur ajoutée, suggérant que l’utilisation actuelle de l’IA est la plus répandue dans les tâches cognitives et analytiques [3].

Dans le domaine des statistiques officielles, le FMI a lancé StatGPT, une initiative qui exploite les LLM pour générer des requêtes structurées via les API des agences statistiques officielles [4]. Cette approche garantit que les utilisateurs reçoivent les chiffres publiés exacts tout en bénéficiant d’une interaction en langage naturel, surpassant les limitations des applications GenAI prêtes à l’emploi qui fournissent fréquemment des chiffres erronés [4].

Par ailleurs, le Committee on National Statistics, le Federal Committee on Statistical Methodology et le National Institute of Statistical Sciences organisent un second AI Day pour les statistiques fédérales le 30 avril 2026 [5]. Cet atelier explorera les implications de l’IA pour les statistiques fédérales, offrant des opportunités de formation, de renforcement des capacités et de partage des meilleures pratiques pour utiliser l’IA afin d’améliorer l’efficacité gouvernementale et moderniser la main-d’œuvre fédérale [5].

Références

[1] AI Can Help with Survey Writing, But It Still Requires Human Expertise. Nielsen Norman Group. https://www.nngroup.com/articles/ai-survey-writing/

[2] Trusting your LLM: AI’s handling of complex statistical data. Mathematica. https://www.mathematica.org/blogs/trusting-your-llm

[3] Monitoring AI Adoption in the US Economy. Federal Reserve. https://www.federalreserve.gov/econres/notes/feds-notes/monitoring-ai-adoption-in-the-u-s-economy-20260403.html

[4] StatGPT: AI for Official Statistics. International Monetary Fund. https://www.imf.org/en/publications/departmental-papers-policy-papers/issues/2026/03/10/statgpt-ai-for-official-statistics-573514

[5] AI Day for Federal Statistics 2026. Population Association of America. https://www.populationassociation.org/events/event-description?CalendarEventKey=f26dfb08-99f4-42fa-921a-019cb515a57b&Home=%2Fhome

Contact: bakodramane@gmail.com

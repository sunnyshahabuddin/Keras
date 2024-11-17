%-------------------------
% Resume in Latex
% Author : Sunny Shahabuddin
% License : MIT
%------------------------

\documentclass[letterpaper,9pt]{article}

\usepackage{latexsym}
\usepackage[empty]{fullpage}
\usepackage{titlesec}
\usepackage{marvosym}
\usepackage[usenames,dvipsnames]{color}
\usepackage{verbatim}
\usepackage{enumitem}
\usepackage[hidelinks]{hyperref}
\usepackage[english]{babel}
\usepackage{tabularx}
% \usepackage{fontawesome5}
\usepackage{multicol}
\usepackage{graphicx}
\setlength{\multicolsep}{-3.0pt}
\setlength{\columnsep}{-1pt}
\input{glyphtounicode}

\RequirePackage{tikz}
\RequirePackage{xcolor}
\RequirePackage{fontawesome}
\definecolor{cvblue}{HTML}{0E5484}
\definecolor{black}{HTML}{130810}
\definecolor{darkcolor}{HTML}{0F4539}
\definecolor{cvgreen}{HTML}{3BD80D}
\definecolor{taggreen}{HTML}{00E278}
\definecolor{SlateGrey}{HTML}{2E2E2E}
\definecolor{LightGrey}{HTML}{666666}
\colorlet{name}{black}
\colorlet{tagline}{darkcolor}
\colorlet{heading}{darkcolor}
\colorlet{headingrule}{cvblue}
\colorlet{accent}{darkcolor}
\colorlet{emphasis}{SlateGrey}
\colorlet{body}{LightGrey}



%----------FONT OPTIONS----------
% sans-serif
% \usepackage[sfdefault]{FiraSans}
% \usepackage[sfdefault]{roboto}
% \usepackage[sfdefault]{noto-sans}
% \usepackage[default]{sourcesanspro}

% serif
% \usepackage{CormorantGaramond}
% \usepackage{charter}


% \pagestyle{fancy}
% \fancyhf{}  % clear all header and footer fields
% \fancyfoot{}
% \renewcommand{\headrulewidth}{0pt}
% \renewcommand{\footrulewidth}{0pt}

% Adjust margins
\addtolength{\oddsidemargin}{-0.6in}
\addtolength{\evensidemargin}{-0.5in}
\addtolength{\textwidth}{1.3in}
\addtolength{\topmargin}{-.8in}
\addtolength{\textheight}{1.4in}

\urlstyle{same}

\raggedbottom
\raggedright
\setlength{\tabcolsep}{0in}

% Sections formatting
\titleformat{\section}{
  \vspace{-4pt}\scshape\raggedright\large\bfseries
}{}{0em}{}[\color{black}\titlerule \vspace{-5pt}]

% Ensure that generate pdf is machine readable/ATS parsable
\pdfgentounicode=1

%-------------------------
% Custom commands
\newcommand{\resumeItem}[1]{
  \item\small{
    {#1 \vspace{-2pt}}
  }
}

\newcommand{\classesList}[4]{
    \item\small{
        {#1 #2 #3 #4 \vspace{-2pt}}
  }
}

\newcommand{\resumeSubheading}[4]{
  \vspace{-2pt}\item
    \begin{tabular*}{1.0\textwidth}[t]{l@{\extracolsep{\fill}}r}
      \textbf{\large#1} & \textbf{\small #2} \\
      \textit{\large#3} & \textit{\small #4} \\
      
    \end{tabular*}\vspace{-7pt}
}

\newcommand{\resumeSubSubheading}[2]{
    \item
    \begin{tabular*}{0.97\textwidth}{l@{\extracolsep{\fill}}r}
      \textit{\small#1} & \textit{\small #2} \\
    \end{tabular*}\vspace{-7pt}
}


\newcommand{\resumeProjectHeading}[2]{
    \item
    \begin{tabular*}{1.001\textwidth}{l@{\extracolsep{\fill}}r}
      \small#1 & \textbf{\small #2}\\
    \end{tabular*}\vspace{-7pt}
}

\newcommand{\resumeSubItem}[1]{\resumeItem{#1}\vspace{-4pt}}

\renewcommand\labelitemi{$\vcenter{\hbox{\tiny$\bullet$}}$}
\renewcommand\labelitemii{$\vcenter{\hbox{\tiny$\bullet$}}$}

\newcommand{\resumeSubHeadingListStart}{\begin{itemize}[leftmargin=0.0in, label={}]}
\newcommand{\resumeSubHeadingListEnd}{\end{itemize}}
\newcommand{\resumeItemListStart}{\begin{itemize}}
\newcommand{\resumeItemListEnd}{\end{itemize}\vspace{-5pt}}


\newcommand\sbullet[1][.5]{\mathbin{\vcenter{\hbox{\scalebox{#1}{$\bullet$}}}}}

%-------------------------------------------
%%%%%%  RESUME STARTS HERE  %%%%%%%%%%%%%%%%%%%%%%%%%%%%


\begin{document}

%----------HEADING----------


\begin{center}
    {\Huge \scshape Sunny Shahabuddin} \\ \vspace{1pt}
    \small \href{tel:+917070560616}{ \raisebox{-0.1\height}\faPhone\ \underline{+91-7070560616} ~} \href{sunny786shahabuddin@gmail.com}{\raisebox{-0.2\height}\faEnvelope\  \underline{sunny786shahabuddin@gmail.com}} ~ 
    \href{https://linkedin.com/in/sunnyshahabuddin/}{\raisebox{-0.2\height}\faLinkedinSquare\ \underline{sunnyshahabuddin}}  ~
    \href{https://github.com/sunnyshahabuddin}{\raisebox{-0.2\height}\faGithub\ \underline{sunnyshahabuddin}} ~
    \vspace{-4pt}
\end{center}

%-----------EXPERIENCE-----------
\section{EXPERIENCE}
\resumeSubHeadingListStart
  \resumeSubheading
    {Barclays}{01 2023 -- Present}
    {\underline{Software Engineer: BA3}}{Pune, India}
    \vspace{0.2pt}
    \resumeItemListStart
      \resumeItem{\textbf{Central Bank of Ireland Statistical Reporting:}}
      \resumeItemListStart
        \resumeItem{\small{Streamlined the application by restructuring the mappings in collaboration with \textbf{stakeholders}.}}
        \resumeItem{\small{Built \textbf{automations} in Axiom to resolve negatives in reports and reconcile data, saving \textbf{12 man-days} per month.}}
        \resumeItem{\small{Implemented \textbf{mandatory patches} in Axiom for regulatory changes and enhancements.}}
        \resumeItem{\small{Built controls to \textbf{restrict irrelevant data flow} for CBI reporting and automated statistical reports.}}
        \resumeItem{\small{Provided \textbf{submission support}, trained teammates on the process, and explained application data flow.}}
        \resumeItem{\small{Maintained infrastructure by \textbf{purging older instances} and synchronizing environments.}}
        \resumeItem{\small{Integrated \textbf{CI/CD pipelines} using Jenkins to improve deployment efficiency.}}
      \resumeItemListEnd
      \vspace{3pt}
      \resumeItem{\textbf{Bank of England Statistical Reporting:}}
      \resumeItemListStart
        \resumeItem{\small{Built movement reports in \textbf{Axiom CV10}, highlighting differences and threshold breaches across reporting periods.}}
        \resumeItem{\small{Fixed API certificate issues and ensured smooth functionality post \textbf{JDK updates}.}}
        \resumeItem{\small{Upgraded infrastructure by \textbf{adding storage} and upgrading the Axiom version.}}
        \resumeItem{\small{Resolved a critical production issue related to incorrect flow of interest without the principal amount.}}
        \resumeItem{\small{Worked on \textbf{machine learning POC} to predict values for the next reporting period, with threshold breach identification.}}
      \resumeItemListEnd
      \vspace{3pt}
      \resumeItem{\textbf{Time Series Analysis:}}
      \resumeItemListStart
        \resumeItem{\small{Designed \textbf{machine learning application} to forecast numbers and raise exceptions based on historical data.}}
        \resumeItem{\small{Implemented models like \textbf{LSTM}, Simple Moving Average, Random Forest Regressor, and Holt's Winter Additive.}}
        \resumeItem{\small{Developed APIs to enable the application as a service between multiple machines.}}
        \resumeItem{\small{Created \textbf{user interface} in ReactJS to onboard new applications, modify thresholds, and input daily data for predictions.}}
      \resumeItemListEnd
      \vspace{3pt}
      \resumeItem{\textbf{EiE Dashboard (Excellence in Execution Dashboard):}}
      \resumeItemListStart
        \resumeItem{\small{Migrated the dashboard from Flask-based architecture to open-source technologies like \textbf{Angular}, \textbf{ExpressJS}, and \textbf{MySQL}.}}
        \resumeItem{\small{Automated data fetching from \textbf{ds-insight} with controls to prevent data duplication.}}
        \resumeItem{\small{Built drill-down views for \textbf{CIO, Global Lead, and application levels}, offering tailored insights.}}
        \resumeItem{\small{Added features to visualize \textbf{historical data trends} using various graphs and tables.}}
      \resumeItemListEnd
      \vspace{3pt}
      \resumeItem{\textbf{TCO Dashboard (Total Cost of Ownership Dashboard):}}
      \resumeItemListStart
        \resumeItem{\small{Implemented \textbf{SSO authentication} and functional group controls for different user types.}}
        \resumeItem{\small{Productionized the dashboard using \textbf{NSSM}, enabling auto-restart to minimize service outages.}}
      \resumeItemListEnd
    \resumeItemListEnd
\resumeSubHeadingListEnd

   \resumeSubHeadingListStart
    \resumeSubheading
      {BigBinary}{08 2022 -- 12 2022}
      {\underline{Software Engineer}}{Pune, India}
      \vspace{0.2pt}
      \resumeItemListStart
        \resumeItem{\normalsize{Completed \textbf{two months} of extensive training on \textbf{ReactJS and Ruby on Rails}.}}
        \resumeItem{\normalsize{Built \textbf{Scribble}- full-stack web application built using \textbf{ReactJS, Ruby on Rails, Tailwind CSS}.}}
        \resumeItem{\normalsize A \textbf{password-protected knowledge base} that has two levels of users and views, namely Admin and End-User.}
        \resumeItem{\normalsize Admin can write articles, save them as drafts or directly publish them to the web, schedule an article to be published at a selected time, handle by \textbf{rails worker}.}
        \resumeItem{\normalsize{Added ability to keep track of versions using \textbf{paper trail gem}.}}
        \resumeItem{\normalsize Added ability to store \textbf{authentication token on browser local storage to make the session persistent}.} 
      \resumeItemListEnd  
  \resumeSubHeadingListEnd
% \vspace{-14pt}

%-----------PROGRAMMING SKILLS-----------
\section{TECHNICAL SKILLS}
 \begin{itemize}[leftmargin=0.15in, label={}]
    \small{\item{
     \textbf{\normalsize{Technologies/Frameworks:}}{\normalsize{ Axiom CV10, ReactJS, Flask, Tailwind CSS, Flutter}} \\
     \textbf{\normalsize{Languages:}}{ \normalsize{JavaScript, Python, HTML, CSS, SQL}} \\ 
     \textbf{\normalsize{Developer Tools:}}{ \normalsize{Git, GitHub, BitBucket, Docker, Jenkins, VS Code, Android Studio}} \\
    }}
 \end{itemize}
 \vspace{-15pt}

%-----------EDUCATION-----------
\section{EDUCATION}
\resumeSubHeadingListStart
  \resumeSubheading
    {\small School of Engineering, Cochin University of Science and Technology}{07 2018 -- 06 2022}
    {B.Tech in Information Technology - \textbf{\small CGPA} - \textbf{\small 9.02}}{Kochi, Kerala}
\resumeSubHeadingListEnd
\vspace{-7pt}
\resumeSubHeadingListStart
  \resumeSubheading
    {\small M.S. Memorial Academy}{05 2017}
    {Higher Secondary Education - \textbf{\small Percentage} - \textbf{\small 80\%}}{Patna, Bihar}
\resumeSubHeadingListEnd
\vspace{-7pt}
\resumeSubHeadingListStart
  \resumeSubheading
    {\small Don Bosco Academy}{05 2015}
    {Secondary Education - \textbf{\small Percentage} - \textbf{\small 93.4\%}}{Patna, Bihar}
\resumeSubHeadingListEnd
  
%-----------PERSONAL PROJECTS-----------
\section{PERSONAL PROJECTS}
    \vspace{-3pt}
    \resumeSubHeadingListStart
       \resumeProjectHeading
          {{\textbf{\large{\underline{JobSquare}}} \href{Project Link}{\raisebox{-0.1\height}}} $|$ \large{\underline{Flutter Framework, Firebase Firestore}}}{01 2021 - 05 2021}
          \vspace{-8pt}
          \resumeItemListStart
            \resumeItem{\normalsize{Students can apply for jobs by just \textbf{right-swiping} a company card.}}
            \resumeItem{\normalsize{Resume is automatically sent to the company when a student right-swipes a company, with \textbf{real-time notification}.}}
            \resumeItem{\normalsize{Company can accept or reject a student application by \textbf{right swipe or left swipe} respectively.}}
            \resumeItem{\normalsize{Students can build their resume using the \textbf{in-built resume builder}.}}
          \resumeItemListEnd 
          \vspace{-13pt}
          
       \resumeProjectHeading
          {{\textbf{\large{\underline{HawkEye}}} \href{Project Link}{\raisebox{-0.1\height}}}}{02 2022 - 06 2022}
          \vspace{-8pt}
          \resumeItemListStart
            \resumeItem{\normalsize{Trained a \textbf{Deep Learning Model} that can identify between 43 different traffic signs.}}
            \resumeItem{\normalsize{Used \textbf{Udacity Simulator} for car simulation.}}
            \resumeItem{\normalsize{Data was collected with the help of \textbf{three cameras }mounted on the simulation car, later clean using \textbf{Pandas}}}
            \resumeItem{\normalsize{Simulated a fully functional Self-Driving Car with \textbf{Convolutional Neural Networks and Computer Vision}.}}
          \resumeItemListEnd 
          \vspace{-13pt}
          
    \resumeSubHeadingListEnd
\end{document}

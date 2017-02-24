---
layout: post
title: Statistik - Klausur
slug: statistik-vorlesung
author: Martin Thoma
date: 2017-01-15 17:30
category: German posts
tags: Klausur, Statistik
featured_image: logos/klausur.png
---
<div class="info">Dieser Artikel beschäftigt sich mit der Vorlesung &bdquo;Statistik&ldquo; am KIT. Er dient als Prüfungsvorbereitung. Ich habe die Vorlesungen bei <a href="http://www.math.kit.edu/stoch/~klar/de">Herrn Prof. Dr. Bernhard Klar</a> im Wintersemester 2016 / 2017 gehört. Der Artikel ist noch am Entstehen</div>

## Behandelter Stoff

### Kapitel 0: Vorwissen

<dl>
    <dt><dfn id="empirisches-quartil">Empirisches $p$-Quantil</dfn></dt>
    <dd>
        Das empirische $p$-Quantil, $0 < p < 1$, ist definiert durch

        $$x_p := \begin{cases}x_{(\lceil n p\rceil)} & n \cdot p \notin \mathbb{N}\\
                              \frac{1}{2} \left ( x_{(np)} + x_{(np + 1)}\right ) & n \cdot p \in \mathbb{N}\end{cases}$$
    </dd>
    <dt><dfn>Unteres Quartil</dfn></dt>
    <dd>$$x_{1/4}$$</dd>
    <dt><dfn>Empirischer Median</dfn></dt>
    <dd>$$x_{1/2}$$</dd>
    <dt><dfn>Rechenregeln für Covarianz</dfn></dt>
    <dd>

        $$C(U_1 + U_2, V) = C(U_1, V) + C(U_2, V)$$
        $$C(AU, B^T V) = A C(U, V) B$$

    </dd>
    <dt><a href="https://de.wikipedia.org/wiki/Normalverteilung"><dfn id="normalverteilug">Normalverteilung</dfn></a></dt>
    <dd>

        Dichte:

        $$f(x) = \frac{1}{\sigma \sqrt{2 \pi}} e^{- \frac{1}{2} {\left ( \frac{x-\mu}{\sigma} \right )}^2}$$

    </dd>
    <dt><a href="https://de.wikipedia.org/wiki/Korrelationskoeffizient#Definitionen"><dfn id="korrelationskoeffizient">Korrelationskoeffizient</dfn></a></dt>
    <dd>$$\rho_{X,Y} =\frac{\operatorname{Cov}(X,Y)}{\sqrt{\operatorname{Var}(X)\operatorname{Var}(Y)}}=\frac{\sigma_{X,Y}^2}{\sigma_{X}\sigma_{Y}}$$</dd>
<!--     <dt><dfn>Rechenregeln Multivariate Normalverteilung</dfn></dt>
    <dd>



    </dd> -->
</dl>


### Kapitel 1: Parameter&shy;schätzung

<dl>
    <dt><dfn>Stichprobenraum</dfn></dt>
    <dd>Der Stichprobenraum $\mathfrak{X}$ ist eine Menge von Daten.</dd>
    <dt><dfn id="statistisches-modell">Statistisches Modell</dfn></dt>
    <dd>Ein Tupel $(\mathfrak{X}, (P_\theta)_{\theta \in \Theta})$ heißt
        <i>statistisches Modell</i>, wenn $\mathfrak{X}$ ein Stichprobenraum
        und $(P_\theta)_{\theta \in \Theta}$ eine Familie von
        Verteilungen $P_\theta$ ist, welche durch $\theta \in \Theta$
        parametrisiert ist.
        </dd>
    <dt><dfn>Schätzer</dfn></dt>
    <dd>Sei $(\mathfrak{X}, (P_\theta)_{\theta \in \Theta})$ ein statistisches
        Modell und $T: \mathfrak{X} \rightarrow \tilde{\Theta}$ eine Abbildung.
        Dann heißt $T$ ein Schätzer für $\theta$.</dd>
    <dt><dfn id="maximum-likelihood-estimator">Maximum-Likelihood-Schätzer</dfn></dt>
    <dd>

    <ol>
        <li><b>Likelihood-Funktion</b>: Multipliziere die Wahrscheinlichkeit der Werte um $L_x(\vartheta)$ zu bestimmen</li>
        <li><b>Log-Likelihood</b>: Logarithmiere die Likelihood-Funktion $l_x(\vartheta) = \log L_x(\vartheta)$, falls dadurch die Funktion vereinfacht wird</li>
        <li><b>Maximieren</b>: Leite die (Log)likelihood-Funktion ab und setze sie gleich 0 um
            den Maximum-Likelihood-Schätzer $\hat{\vartheta}$ zu bestimmen.</li>
        <li><b>Maximalstelle</b>: Prüfe ob zweite Ableitung negativ ist</li>
    </ol>

    </dd>
    <dt><dfn id="momentenschaetzer">Momentenschätzer</dfn></dt>
    <dd>

    <ol>
        <li>Es sollen z.B. $\mu$ und $\sigma^2$ geschätzt werden.</li>
        <li>Drücke $\mu$ und $\sigma^2$ als Funktion der Momente $E X$, $E X^2$, ... aus.</li>
    </ol>

    Nützlich: $V(X) = E X^2 - (E X)^2$

    </dd>
    <dt><a href="https://de.wikipedia.org/wiki/Starkes_Gesetz_der_gro%C3%9Fen_Zahlen#Formulierung"><dfn>Starkes Gesetz großer Zahlen</dfn></a></dt>
    <dd>Es seien $Y_1, Y_2, Y_3, \dots$ eine Folge u.i.v. ZV mit existierendem
        Erwartungswert. Dann gilt:
        $$P(\left \{ \omega \in \Omega : \lim_{n \rightarrow \infty} \frac{1}{n} \sum_{i=1}^n Y_i(\omega) = E Y_i \right \}) = 1$$

        Schreibweise:
        $$\frac{1}{n} \sum_{i=1}^n Y_i \stackrel{P-f.s.}{\longrightarrow} E(Y_1)$$
        </dd>
    <dt><dfn id="score-funktion">Score-Funktion</dfn></dt>
    <dd>$$U_\vartheta(X_1) := \frac{\partial \log f(X_1, \vartheta)}{\partial \vartheta}$$</dd>
    <dt><dfn id="fisher-information">Fisher-Information</dfn></dt>
    <dd>$$I(\vartheta) := \mathbb{E}_\vartheta(U_\vartheta^2) = - \mathbb{E}_\vartheta \left [ \frac{\partial U_\vartheta (X_1)}{\partial \vartheta} \right ] \in [0, \infty]$$</dd>
    <dt><dfn id="cramer-rao">Cramér-Rao Ungleichung</dfn></dt>
    <dd>$$V_\vartheta(T) \geq \frac{[E_\vartheta' (T) (\vartheta)]^2}{n I (\vartheta)}$$

        Für erwartungstreue Schätzer $T$ gilt:
        $$V_\vartheta(T) \geq \frac{1}{n I (\vartheta)}$$
    </dd>
    <dt><a href="https://de.wikipedia.org/wiki/Cauchy-Schwarzsche_Ungleichung"><dfn>Cauchy-Schwarz Ungleichung</dfn></a></dt>
    <dd>$$|\langle x, y \rangle | \leq \| x \| \cdot \| y \|$$</dd>
    <dt><a href="https://de.wikipedia.org/wiki/Zentraler_Grenzwertsatz"><dfn>Zentraler Grenzwertsatz</dfn></a> (<dfn id="zgws">ZGWS</dfn>)</dt>
    <dd>Sei $(X_n)_{n \geq 1}$ eine Folge von u.i.v. Zufallsvariablen mit
        $0 < \sigma^2 = V(X_1) < \infty $. Mit $\mu = \mathbb{E}(X_1)$ gilt
        dann:
        $$P(\frac{\sqrt{n}(\bar{X}_n - \mu)}{\sigma} < c) \stackrel{n \rightarrow \infty}{\longrightarrow} \Phi(c)$$</dd>
    <dt><dfn>Verteilungskonvergenz</dfn></dt>
    <dd>TODO</dd>
    <dt><dfn>Score-Gleichung</dfn></dt>
    <dd>Score-Funktion gleich 0 setzen:
        $$\sum_{i=1}^n \frac{\partial f(x_i, \vartheta)}{\partial \vartheta} = 0$$
    </dd>
    <dt><dfn>Bias</dfn> (<dfn>Verzerrung</dfn>)</dt>
    <dd>$$b_T(\vartheta) := E_\vartheta(T) - \gamma(\vartheta)$$</dd>
    <dt><dfn>Mittlere Quadratische Abweichung</dfn> (<dfn id="mqa">MQA</dfn>)</dt>
    <dd>
    $$MQA_T(\vartheta) = E_\vartheta(T - \gamma(\vartheta))^2$$


    Es gilt:
    $$MQA_T(\vartheta) = V_\vartheta(T) + b_T^2 (\vartheta)$$
    </dd>
    <dt><dfn>Satz 1.7.5</dfn> (<dfn>Asymptotische Verteilung konsistenter Schätzer</dfn>)</dt>
    <dd>$$\sqrt{n} (\hat{\vartheta}_n - \vartheta) \stackrel{D_\vartheta}{\rightarrow} \mathcal{N}(0, \frac{1}{I_1 (\vartheta)})$$</dd>
</dl>


### Kapitel 2: Konfidenz&shy;bereiche

<dl>
    <dt><dfn id="konfidenzintervall">Konfidenzintervall</dfn> (<dfn>Vertrauensintervall</dfn>)</dt>
    <dd>

        Ein Konfidenzintervall ist ein Intervall $[U, O]$ für einen Parameter
        $\vartheta$, sodass gilt:

        $$P([U, O] \ni \vartheta) = 1 - \alpha$$

        <ul>
            <li>1-Stichproben-t-Test: $I(X) = \left [\bar{X} - \frac{S}{\sqrt{n}} \cdot t_{n-1;1-\frac{\alpha}{2}}, \bar{X} + \frac{S}{\sqrt{n}} \cdot t_{n-1;1-\frac{\alpha}{2}} \right]$</li>
            <li>Approximativer Binomialtest: $I(X) = \left [ \hat{p}_n - z_{1-\frac{\alpha}{2}} \sqrt{\hat{p}_n (1- \hat{p}_n)/n}, \hat{p}_n + z_{1-\frac{\alpha}{2}} \sqrt{\hat{p}_n (1- \hat{p}_n) / n} \right ]$</li>
        </ul>
    </dd>
    <dt><dfn id="satz-von-student">Satz von Student</dfn></dt>
    <dd>Es seien $X_1, X_2, \dots, X_n \stackrel{uiv}{\sim} \mathcal{N}(\mu, \sigma^2),\quad n\geq 2$ sowie $\bar{X} = \frac{1}{n} \sum_{i=1}^n X_i$, $S^2 = \frac{1}{n-1} \sum_{i=1}^n {(X_i - \bar{X})}^2$ sowie $S = \sqrt{S^2}$. Dann gilt:

    <ol>
        <li>$\bar{X} \sim \mathcal{N}(\mu, \frac{\sigma}{n})$</li>
        <li>$\bar{X}$ und $S^2$ sind unabhängig</li>
        <li>$\frac{1}{\sigma^2} \sum_{i=1}^n {(X_i - \bar{X})}^2 \sim \chi_{n-1}^2$</li>
        <li>$T = \frac{\sqrt{n} (\bar{X} - \mu)}{S} \sim t_{n-1}$</li>
    </ol>

    </dd>
</dl>


### Kapitel 3: Statistische Tests

TODO

<dl>
    <dt><dfn>Tests Allgemein</dfn></dt>
    <dd>

        Bei statistischen Tests hat man immer eine Testgröße $T(x_1, \dots,
        x_n)$, die auf der Stichprobe $x_1, \dots, x_n$ basiert. Um Aussagen
        machen zu können, muss man die Verteilung von $T$ unter der
        Nullhypothese $H_0$ kennen. Wenn die Verteilung von $T$ der
        Studentischen-$t$-Verteilung entspricht ($T \sim t_n$), dann hat man
        einen $t$-Test.<br/>
        <br/>
        Wenn der Testentscheid, ob $H_0$ verworfen wird so
        aussieht:
        $$H_0 \text{ wird verworfen, falls } T < 123$$
        dann liegt ein einseitiger Test vor.
        Falls der Testentscheid, ob $H_0$ verworfen wird so
        aussieht:
        $$H_0 \text{ wird verworfen, falls } T < -123 \text{ oder } T > +123$$
        dann liegt ein zweiseitiger Test vor. Kurz schreibt man dann auch meistens
        $$H_0 \text{ wird verworfen, falls } |T| > 123$$
        <br/>
        In dem beschriebenen Fall liegt eine Stichprobe $X_1, \dots, X_n$ vor,
        welche aus einer Verteilung gezogen wurde. Es ist aber auch möglich,
        dass man zwei Stichproben $X_1, \dots, X_n$ und $Y_1, \dots, Y_m$ hat.
        Das ist z.B. bei Medikamententests häufig der Fall. Da will man wissen
        ob beide Stichproben aus der gleichen Verteilung stammen (also das
        Medikament nichts macht) oder eben nicht.

    </dd>
    <dt><dfn>$z$-Test</dfn></dt>
    <dd>

        <ul>
            <li>Hypothesen: $H_0$: $\mu = \mu_0$ vs $H_1: \mu < \mu_0$</li>
            <li>Testgröße: $T(x_1, \dots, x_n) = \frac{\sqrt{n} (\bar{x} - \mu_0)}{\sigma}$</li>
            <li>Verteilung: $T \stackrel{H_0}{\sim} \mathcal{N}(0, 1)$</li>
            <li>Testentscheid: $H_0$ verwerfen, falls $T \leq \Phi^{-1}(\alpha) = z_\alpha$</li>
        </ul>

    </dd>
    <dt><dfn>Zweiseitiger Ein-Stichproben-$t$-Test</dfn></dt>
    <dd>

        <ul>
            <li>Testgröße: $T(x_1, \dots, x_n) = \frac{\sqrt{n} (\bar{x} - \mu_0)}{s}$</li>
            <li>Verteilung: $T \stackrel{H_0}{\sim} t_{n-1}$</li>
            <li>Testentscheid: $H_0$ verwerfen, falls $|T| \geq t_{n-1; 1-\frac{\alpha}{2}}$</li>
        </ul>

    </dd>
    <dt><dfn>Einseitiger Ein-Stichproben-$t$-Test</dfn></dt>
    <dd>

        <ul>
            <li>Testgröße: $T(x_1, \dots, x_n) = \frac{\sqrt{n} (\bar{x} - \mu_0)}{s}$</li>
            <li>Verteilung: $T \stackrel{H_0}{\sim} t_{n-1}$</li>
            <li>Testentscheid: $H_0$ verwerfen, falls $T \geq t_{n-1; 1-\alpha}$</li>
        </ul>

    </dd>
    <dt><dfn>Ein-Stichproben-Varianz-Test</dfn></dt>
    <dd>

        <ul>
            <li>Hypothesen: $H_0: \sigma^2 = \sigma_0^2$ gegen $H_1: \sigma^2 > \sigma_0^2$</li>
            <li>Testgröße: $\chi^2 := \frac{(n-1)S^2}{\sigma_0^2}$</li>
            <li>Verteilung: $\chi^2 \stackrel{H_0}{\sim} \chi_{n-1}^2$</li>
            <li>Testentscheid: $H_0$ verwerfen, falls $\chi^2 \geq \chi^2_{n-1;1-\alpha}$</li>
        </ul>

    </dd>
    <dt><a href="https://de.wikipedia.org/wiki/G%C3%BCtefunktion"><dfn id="guetefunktion">Gütefunktion</dfn></a></dt>
    <dd>Die Gütefunktion ist $g(\vartheta) = P_\vartheta(\text{Test verwirft } H_0), \quad \vartheta \in \Theta$.</dd>
    <dt><dfn id="neyman-pearson-test">Neyman-Pearson-Test</dfn> (<dfn>NP-Test</dfn>)</dt>
    <dd>

        Sei $h_0(x) = \prod_{i=1}^n f(x, \vartheta_0)$ und
        $h_1(x) = \prod_{i=1}^n f(x, \vartheta_1)$.<br/>
        <br/>
        Testentscheid: Verwerfe $H_0$, falls $h_0(x) \leq c h_1(x)$, wobei
        $c$ so gewählt wird, dass das Niveau $\alpha$ eingehalten wird.

    </dd>
    <dt><dfn id="likelihood-quotienten-test">Likelihood-Quotienten-Test</dfn></dt>
    <dd>
        <ul>
            <li>Testgröße: $$\Lambda = \frac{\sup_{\vartheta \in \Theta} L_x (\vartheta)}{\sup_{\vartheta \in \Theta_0} L_x (\vartheta)}$$</li>
            <li>Hypothesen: $H_0$: $\vartheta \in \Theta_0$ vs $H_1$: $\vartheta \in \Theta \setminus \Theta_0$</li>
            <li>Verteilung: Ist der Schätzer konsistent, so gilt $$2 \log(\Lambda_n) \sim \chi_1^2$$</li>
            <li>Testentscheid: Verwerfe $H_0$, falls $\Lambda > c$.
                Wähle $c$ so, dass Niveau $\alpha$ eingehalten wird.<br/>
                Also: Verwerfe $H_0$, falls
                $2 \log \Lambda_n \geq \chi^2_{1, 1-\alpha}$</li>
        </ul>
    </dd>
    <dt><dfn id="approximativer-binomialtest">Approximativer Binomialtest</dfn></dt>
    <dd>
        Gegeben seien $X_1, \dots, X_n \sim Bin(1, p)$, $p$ unbekannt.

        <ul>
            <li>Hypothesen: $H_0: p = p_0$ vs $H_1: p = p_1$</li>
            <li>Testgröße: $T_n(x) = \frac{\sqrt{n}(\bar{X} - p)}{\sqrt{p (1-p)}}$</li>
            <li>Verteilung: $T_n \stackrel{H_0}{\sim} \mathcal{N}(0, 1)$</li>
            <li>Testentscheid: $H_0$ verwerfen, falls $T_n > z_{1-\alpha}$</li>
        </ul>

    </dd>
</dl>


### Kapitel 4: 2-Stichproben Vergleiche (NV)

TODO

<dl>
    <dt><dfn id="f-test-varianzquotient">F-Test für den Varianzquotienten</dfn></dt>
    <dd>

        Gegeben sind zwei Stichproben $X_1, \dots, X_m$ sowie $Y_1, \dots, Y_n$
        mit $X_i \sim \mathcal{N}(\mu, \sigma^2)$ und $\mathcal{N}(\nu, \tau^2)$.

        <ul>
            <li>Hypothesen: $H_0: \sigma^2 = \tau^2$ vs $H_1: \sigma^2 \neq \tau^2$</li>
            <li>Testgröße:
        $$Q_{m,n} = \frac{\frac{1}{m-1} \sum_{i=1}^m {(X_i - \bar{X}_m)}^2}{\frac{1}{n-1} \sum_{i=1}^n {(Y_i - \bar{Y}_n)}^2}$$</li>
            <li>Verteilung: $Q_{m,n} \stackrel{H_0}{\sim} F_{m-1, n-1}$</li>
            <li>Testentscheid: $H_0$ verwerfen, falls $Q_{m,n} \leq F_{m-1,n-1;\frac{\alpha}{2}}$ oder $Q_{m,n} \geq F_{m-1,n-1;1-\frac{\alpha}{2}}$</li>
        </ul>
    </dd>
</dl>


### Kapitel 5: Lineare Regression
TODO

<dl>
    <dt>Satz 5.4.1</dt>
    <dd>Unter $H_0$ ist die Teststatistik $F = \frac{(RSS_r - RSS)/(p-r)}{RSS/(n-p)}$ Fisher-verteilt mit $p-r$ Zähler- und $n-p$ Nenner-Freiheitsgraden.</dd>
    <dt id="anova-tafel">ANOVA-Tafel</dt>
    <dd>
        <table class="table">
            <tr>
                <td>&nbsp;</td>
                <th>Freiheitsgrade</th>
                <th>Quadratsumme</th>
                <th>mittlere Quadratsumme</th>
                <th>Teststatistik</th>
            </tr>
            <tr>
                <th>Regression</th>
                <td>$p-1$</td>
                <td>TSS - RSS</td>
                <td>$\frac{TSS-RSS}{p-1}$</td>
                <td>F</td>
            </tr>
            <tr>
                <th>Residuen</th>
                <td>$n-p$</td>
                <td>RSS</td>
                <td>$\frac{RSS}{n-p}$</td>
                <td>&nbsp;</td>
            </tr>
            <tr>
                <th>Gesamt</th>
                <td>$n-1$</td>
                <td>TSS</td>
                <td>&nbsp;</td>
                <td>&nbsp;</td>
            </tr>
        </table>

    </dd>
    <dt><dfn id="least-squares-estimator">Kleinster-Quadrate-Schätzer</dfn></dt>
    <dd>

        Der Kleinste-Quadrate-Schätzer für das klassische lineares Modell
        $Y = X \beta + \epsilon$ lautet:
        $$\hat{\beta} = (X^T X)^{-1} X^T Y$$
        $$\hat{Y} \sim N_n(X \beta, \sigma^2 H)$$

        Es gilt:
        $$\hat{\beta} \sim N_p(\beta, \sigma^2 (X^T X)^-1)$$
        $$\hat{\beta}_i \sim \mathcal{N}(\beta_i, \sigma^2 (X^T X)^{-1}_{i+1, i+1})$$
        sowie
        $$(n-p)\hat{\sigma}^2/\sigma^2 \sim \chi^2_{n-p}$$

        Der übliche Schätzer für $\sigma^2$ ist
        $$\hat{\sigma}^2 = \frac{1}{n-p} \| Y - \hat{Y} \|^2$$
    </dd>
</dl>


### Kapitel 6: Varianz- und Kovarianz&shy;analyse
TODO

<dl>
    <dt><dfn>Modellannahmen der Varianzanalyse</dfn></dt>
    <dd>

        Das Rauschen ist unabhängig und jeweils $\varepsilon_i \sim \mathcal{N}(0, \sigma^2)$.

    </dd>
    <dt><dfn>Summenrestriktionen</dfn></dt>
    <dd>Es muss ein balanciertes Design ($n_1 = n_2 = \dots = n_k$) vorliegen.
        Dann muss
        $$\sum_{i=1}^k \alpha_i = 0$$
        gelten.

        Das Modell ist $Y = X \beta + \varepsilon$ mit Design-Matrix
        $$X = \begin{pmatrix}1      & 1& 0      &        &0\\
                             \vdots & \vdots & \vdots &        &\vdots\\
                             \vdots & 1      & 0      &        &\vdots\\
                             \vdots & 0      & 1      &        &\vdots\\
                             \vdots & \vdots & \vdots &        & \vdots\\
                             \vdots & \vdots & 1      &        & 0\\
                             \vdots & \vdots & 0      &        & 1\\
                             \vdots & \vdots & \vdots & \ddots &\vdots\\
                             \vdots & 0      & 0      &        & 1\\
                             \vdots & -1     & -1     & \dots  & -1\\
                             \vdots & \vdots & \vdots &        & \vdots\\
                             1      & -1     & -1     & \dots  & -1\\\end{pmatrix}$$
        und Parametervektor
        $$\beta := \begin{pmatrix}\mu\\\alpha_2\\\dots\\\alpha_k\end{pmatrix}$$
    </dd>
    <dt><a href="https://de.wikipedia.org/wiki/Bonferroni-Methode"><dfn>Bonferroni-Korrektur</dfn></a></dt>
    <dd>Es liegt eine Familie von $m$ Tests vor. Man macht eine globale Nullhypothese,
        dass alle Nullhypothesen gelten. Alle $m$ Test werden auf dem Niveau
        $\frac{\alpha}{m}$ durchgeführt, sodass insgesamt das Niveau $\alpha$
        erreicht wird.</dd>
    <dt><dfn id="bestimmtheitsmass">Bestimmtheitsmaß $R^2$</dfn></dt>
    <dd>

        $$R^2 = 1 - \frac{RSS}{TSS} = 1 - \frac{\sum_{i=1}^n (y_i - \hat{y}_i)}{\sum_{i=1}^n (y_i - \bar{y}_i)}$$

        Es gilt: $R^2 \in [0, 1]$

        Ist die Kenntnis von $x$ wichtig für die Vorhersage von $y$, so ist das
        Bestimmtheitsmaß nahe bei 1.
    </dd>
    <dt><dfn id="globaler-f-test">Globaler $F$-Test</dfn></dt>
    <dd>

        <ul>
            <li>Hypothesen: $H_0$: $\mu_1 = \mu_2 = \dots = \mu_k$ vs $H_1: \exists i, j: \mu_i \neq \mu_j$</li>
            <li>Testgröße: $F = \frac{(RSS_1 - RSS) / (k-1)}{RSS / (n-k)}$</li>
            <li>Verteilung: $F \stackrel{H_0}{\sim} F_{k-1, n-k}$</li>
            <li>Testentscheid: $H_0$ verwerfen, falls $F \geq F_{k-1, n-k; 1 - \alpha}$</li>
        </ul>

    </dd>
</dl>

### Kapitel 7: Kategoriale Daten
TODO

### Kapitel 8: Nicht&shy;parametrische Verfahren

<dl>
    <dt><dfn id="vorzeichen-test">Vorzeichen-Test für den Median</dfn></dt>
    <dd>
        Teste die Hypothese ob eine Größe $M$ den Mittelwert $\mu$ hat gegen
        die Alternative $H_1$: $M \neq \mu$.
        Bilde die Prüfgröße
        $$S_n = \sum_{i=1}^n \mathbb{1}_{X_i > \mu}$$
        Falls $H_0$ gilt, dann ist $S_n \sim Bin(n, 0.5)$
        Lehne $H_0$ ab, wenn $S_n \leq c$ oder $S_n \geq n - c$. Bestimme $c$
        so, dass
        $$P_{H_0}(S_n \leq c) + P_{H_0}(S_n \geq n - c) \stackrel{!}{\leq} \alpha$$

    </dd>
</dl>


## Abkürzungen

* MQA: Mittlere Quadratische Abweichung
* RSS: Residual Sum of Squares
* SQI: Summe der Quadrate innerhalb der Gruppen
* SQZ: Summe der Quadrate zwischen den Gruppen
* TTS: Total Sum of Squares
* uiv, u.i.v.: unabhängig identisch verteilt


## Symbolverzeichnis

<table class="table">
    <tr>
        <th>Symbol</th>
        <th>Bedeutung</th>
    </tr>
    <tr>
        <td>$c_\alpha$</td>
        <td>$\Phi^{-1}(\alpha)$: Inverse Verteilungsfunktion der Standardnormalverteilung</td>
    </tr>
    <tr>
        <td>$E(X)$</td>
        <td>Erwartungswert der Zufallsvariable $X$</td>
    </tr>
    <tr>
        <td>$\mathcal{N}(\mu, \sigma^2)$</td>
        <td>Normalverteilung mit Mittelwert $\mu$ und Standardabweichung $\sigma$</td>
    </tr>
    <tr>
        <td>$Pois(\lambda)$</td>
        <td>Poisson-Verteilung</td>
    </tr>
    <tr>
        <td>$t_{n; \beta}$</td>
        <td>Das $\beta$-Quantil der $t_n$-Verteilung.</td>
    </tr>
    <tr>
        <td>$V(X)$</td>
        <td>Varianz der Zufallsvariable $X$</td>
    </tr>
    <tr>
        <td>$\mathfrak{X}$</td>
        <td>Stichprobenraum</td>
    </tr>
    <tr>
        <td>$X \sim A$</td>
        <td>Die Zufallsvariable $X$ ist $AB$-Verteilt.</td>
    </tr>
    <tr>
        <td>$z_{1 - \alpha}$</td>
        <td>Inverse quantilsfunktion der Standardnormalverteilung: $z_{1 - \alpha} = \Phi^{-1}(1-\alpha)$</td>
    </tr>
</table>


## Verteilungen

<table>
    <tr>
        <th>Verteilung</th>
        <th>Schreibweise</th>
        <th>$\mathbb{E}(X)$</th>
        <th>$Var(x)$</th>
        <th>Bemerkung</th>
    </tr>
    <tr>
        <td><a href="https://de.wikipedia.org/wiki/Binomialverteilung">Binomial-Verteilung</a></td>
        <td>$X \sim Bin(n, p)$</td>
        <td>$n \cdot p$</td>
        <td>$n \cdot p \cdot (1-p)$</td>
        <td>$n$-maliges Bernoulli-Experiment</td>
    </tr>
    <tr>
        <td><a href="https://de.wikipedia.org/wiki/Poisson-Verteilung">Poisson-Verteilung</a></td>
        <td>$X \sim Pois(\lambda)$</td>
        <td>$\lambda$</td>
        <td>$\lambda$</td>
        <td></td>
    </tr>
    <tr>
        <td><a href="https://de.wikipedia.org/wiki/Exponentialverteilung">Exponential-Verteilung</a></td>
        <td>$X \sim Exp(\lambda)$</td>
        <td>$\frac{1}{\lambda}$</td>
        <td>$\frac{1}{\lambda^2}$</td>
        <td>Zerfall-Prozess</td>
    </tr>
    <tr>
        <td><a href="https://de.wikipedia.org/wiki/Normalverteilung">Normalverteilung</a></td>
        <td>$X \sim \mathcal{N}(\mu, \sigma^2)$</td>
        <td>$\mu$</td>
        <td>$\sigma^2$</td>
        <td></td>
    </tr>
    <tr>
        <td><a href="https://de.wikipedia.org/wiki/Gleichverteilung">Gleichverteilung</a></td>
        <td>$X \sim U[a, b]$</td>
        <td>$\frac{b-a}{2}$</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td><a href="https://de.wikipedia.org/wiki/Chi-Quadrat-Verteilung">$\chi^2$-Verteilung</a></td>
        <td>$X \sim \chi^2_n$</td>
        <td>$n$</td>
        <td>$2n$</td>
        <td>Summe von $n$ normalverteilugen Zuvallsvariablen $X_1, \dots, X_n$</td>
    </tr>
    <tr>
        <td><a href="https://de.wikipedia.org/wiki/Studentsche_t-Verteilung">$t$-Verteilung</a></td>
        <td>$X \sim t_k$</td>
        <td>$n$</td>
        <td>$2n$</td>
        <td>$X = \frac{N}{\sqrt{\frac{Y}{k}}}$ mit $Y \sim \chi^2_k$ und $N \sim \mathcal{N}(0, 1)$</td>
    </tr>
    <tr>
        <td><a href="https://de.wikipedia.org/wiki/F-Verteilung">$F$-Verteilung</a></td>
        <td>$X \sim F_{m,n}$</td>
        <td>$\frac{n}{n-2}$ für $n > 2$</td>
        <td>$\frac{2n^2 (m+n-2)}{m(n-2)^2 (n-4)}$ für $n > 4$</td>
        <td>$X = \frac{\frac{1}{r}R}{\frac{1}{s}S}$ mit $R \sim \chi^2_r$, $S \sim \chi^2_s$</td>
    </tr>
</table>


## Python

You might want to look into [`scipy.stats`](https://docs.scipy.org/doc/scipy/reference/stats.html)
as it offers many convenient functions.

For example, if you have to find the 95%-Quantile of the $F_{k=3,n=19}$ distribution,
this is what you do:

```python
import scipy.stats

# Create a variable representing the distribution
rv = scipy.stats.f(dfn=3, dfd=19)

# Percent point function
rv.ppf(0.95)  # gives 3.1273500051133989
```

## Klausur Aufbau

* Aufgabe 1 und 2
    * [ML-Schätzer bestimmen](#maximum-likelihood-estimator)
    * [Score-Funktion](#score-function) / [Fisher-Information](#fisher-information)
    * [Cramér-Rao-Schranke](#cramer-rao)
    * asymptotisch Erwartungstreue / Konsistenz von Schätzern
    * Erwartungswert, Varianz, [MQA](#mqa) eines Schätzers bestimmen
    * [Momentenschätzer](#momentenschaetzer) bestimmen
* Aufgabe 3
    * [Neyman-Pearson-Test](#neyman-pearson-test)
    * [ZGWS](#zgws)
    * [Likelihood-Quotienten-Test](#likelihood-quotienten-test)
* Aufgabe 4
    * [Statistisches Modell](#statistisches-modell) angeben
    * [Quartile](#empirisches-quartil) und Median einer Stichprobe bestimmen
    * [Vorzeichen-Test](#vorzeichen-test) für Median
* Aufgabe 5
    * [Satz von Student](#satz-von-student)
    * [Konfidenzintervall](#konfidenzintervall)
    * [Gütefunktion](#guetefunktion)
    * Beziehung zwischen Konfidenzintervall und Tests
* Aufgabe 6
    * [Korrelationskoeffizient](#korrelationskoeffizient)
    * [ANOVA-Tafel](#anova-tafel)
    * Modellannahmen bei einfacher Varianzanalyse
* Aufgabe 7
    * Lineares Regressionsmodell
    * [Kleinster-Quadrate-Schätzer](#least-squares-estimator)
    * [Bestimmtheitsmaß](#bestimmtheitsmass)
    * Chi-Quadrat-Test auf Homogenität ($D := \sum_{i=1}^n \frac{n_i {(\hat{p}_i - \hat{p})}^2}{\hat{p} (1 - \hat{p})} \stackrel{H_0}{\sim} \chi^2_{k-1}$)
* Various
    * Exp-Verteilung und Zusammenhang mit Gamma-Verteilung
    * Binomial-Verteilung
    * 1-Stichproben t-Test
    * [F-Test für den Varianzquotienten](#f-test-varianzquotient)
    * [Globaler F-Test](#globaler-f-test)


## Prüfungsfragen
* Kann ein Schätzer Erwartungstreu und Konsistent sein?<br/>
  → Ja. Seien $X_1, \dots, X_n \stackrel{uiv}{\sim} Bin(1, \vartheta)$ mit
     $\vartheta \in (0, 1)$. Sei außerdem $\hat{\vartheta}_n = \frac{1}{n} \sum_{i=1}^n x_i$.
     $\hat{\vartheta}_n$ ist erwartungstreu und konsistent.
* Kann ein Schätzer weder Erwartungstreu noch Konsistent sein?<br/>
  → Ja. Seien $X_1, \dots, X_n \stackrel{uiv}{\sim} Bin(1, \vartheta)$ mit
     $\vartheta \in (0, 1)$. Der Schätzer $\hat{\vartheta} = 0.5$ ist weder
     Erwartungstreu noch konsistent für $\vartheta \neq 0.5$.
* Kann ein Schätzer Erwartungstreu, aber nicht konsistent sein?<br/>
  → Ja. Setting wie zuvor und $\hat{\vartheta} = x_n$ (siehe [math.SE](http://math.stackexchange.com/q/2149771/6876))
* Kann ein Schätzer nicht Erwartungstreu, aber konsistent sein?<br/>
  → Ja. Setting wie zuvor und $\hat{\vartheta} = \frac{1}{n} \sum_{i=1}^n x_i + \frac{1}{n}$ (siehe [math.SE](http://math.stackexchange.com/q/2149771/6876))


## Tips

* Klausur WS 2013 / 2014, Aufgabe 1 und 2 sind lehrreich


## Offene Fragen

* WS 2014 / 2015, A6c: TODO
* WS 2014 / 2015, A7a: Warum ist $(I_n - H) X \beta = 0$?
* WS 2013 / 2014, A3b: Warum gilt das?
* WS 2012 / 2013, A6e: Wie kommt man auf $t_6$?



## Material und Links

* [Vorlesungswebsite](http://www.math.kit.edu/stoch/lehre/stat2016w/)
* [Illias](https://ilias.studium.kit.edu/ilias.php?ref_id=603377&cmd=frameset&cmdClass=ilrepositorygui&cmdNode=75&baseClass=ilRepositoryGUI)
* StackExchange
    * [Percentile vs quantile vs quartile](http://stats.stackexchange.com/q/156778/25741)
    * [When is Fishers exact test used; when are approximative tests used?](http://math.stackexchange.com/q/2120746/6876)
    * [What is the range of values of the Fisher information?](http://math.stackexchange.com/q/2157587/6876)
    * [How can I calculate the distribution of the least-squares estimator $\hat{\beta}$?](http://math.stackexchange.com/q/2159447/6876)
* Blog-Artikel
    * [The Absolute Value Function](https://martin-thoma.com/abs-function/) - vgl. Konfidenzintervalle
    * [The p value](https://martin-thoma.com/p-value/)
* [Anki-Karten](https://ankiweb.net/shared/info/245843947) ([direct download](https://martin-thoma.com/anki/Statistik.apkg))
* [Verteilungsfunktion der Normalverteilung](https://github.com/MartinThoma/LaTeX-examples/tree/master/documents/normal-distribution) als Tabelle
* [Inverse Verteilungsfunktion der Normalverteilung](https://github.com/MartinThoma/LaTeX-examples/tree/master/documents/normal-distribution-z) als Tabelle
* Fehlende Musterlösungen: [KIT-Musterloesungen](https://github.com/MartinThoma/KIT-Musterloesungen/tree/master/Statistik) - Verbesserungshinweise nehme ich immer gerne entgegen (`info@martin-thoma.de`)


## Literatur

* Skript von Dr. B. Klar: Statistik
* [<a href="#ref-bic01-anchor" name="ref-bic01">Bic01</a>] P.J. Bickel and K.A. Doksum. Mathematical statistics, 2nd ed.
* [<a href="#ref-cza11-anchor" name="ref-cza11">Cza11</a>] C. Cazado and T. Schmidt. Mathematische Statistik.


## Übungsbetrieb

Übungsblätter sind freiwillig.


## Termine und Klausurablauf

**Datum**: 01.03.2017, 7:30 - 9:30 Uhr (Quelle: <a href="http://www.math.kit.edu/stoch/lehre/stat2016w/event/statklausur1/">Vorlesungswebsite</a> - Ja, es ist wirklich so früh!)<br/>
**Ort**: <a href="https://www.kithub.de/map/2086">Benz-Hörsaal Geb. 10.21</a><br/>
**Punkte**: 60<br/>
**Zeit**: 2h<br/>
**Punkteverteilung**: TODO<br/>
**Bestehensgrenze**: min 50%<br/>
**Übungsschein**: gibt es nicht<br/>
**Bonuspunkte**: gibt es nicht<br/>
**Nicht vergessen**:

* Studentenausweis
* Taschenrechner
* Uhr
* Brille
* Geodreieck
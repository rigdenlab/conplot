import dash_html_components as html
from components import AutomaticInfoCollectedList
from utils import UrlIndex


def GdprPolicySectionOne():
    return html.P(
        'ConPlot (also referred to as ‘we’ throughout this text) is committed to protect user '
        'data and privacy. The purpose of this text is to provide you with information about '
        'how the data we collect from users of ConPlot is used or shared. We may update this '
        'Privacy Notice from time to time. We encourage you re-visit this text frequently '
        'and take note of the date of the last update on the field above. We do not use or '
        'share any of your personal information for any purpose unrelated to the '
        'functionality of the website; however, we do collect some information to help us '
        'understand how our site is being used in order to improve community support and to '
        'enhance the ConPlot user’s experience when visiting our site.'
        , style={"text-align": "justify"})


def GdprPolicySectionTwo():
    return html.P(
        ['When you browse ConPlot, certain information about your visit will be collected. We '
         'automatically collect and store the following type of information about your visit:',
         AutomaticInfoCollectedList(),
         'This automatically collected information does not identify you personally unless you '
         'include personally identifying information in a support form request; see the “Get '
         'in Touch” policy below for details. We use this information to measure the number '
         'of visitors to our site. '
         'The aggregate data may be included in prospectuses and reports to funding agencies.'
         ], style={"text-align": "justify"})


def GdprPolicySectionThree():
    return html.P(
        'Storing, sharing sessions and any other user account related features of ConPlot require '
        'that you register for an account. To register, you will be required to provide an email address, '
        'a username and a password. By choosing to create a user account you give us permission to retain this '
        'information, which will be used only for verification of you as a user and for anonymous '
        'statistics. We require an email address so we can send you a temporary account password in '
        'case you forget this password. An anonymous email service can be used if you do not want to provide '
        'personally identifying information. Your email address will not be used to send you alerts or '
        'notifications. Any email address provided in this site will only be used to get in touch with you '
        'in case your forget your password or you request assistance from us. We do not sell or distribute '
        'email addresses to third parties. We also ask for a user name when creating an account. We will '
        'not sell or distribute your user name or institution to third parties. When you log '
        'in, the client IP address is recorded. If your user profile personally identifies you, then it may be '
        'possible to associate you with your detailed activity on the ConPlot website. After registering as a '
        'user, by choosing to store a session you give us permission to retain the data you provided '
        'within that session. This includes the contents and file names of all the files you have uploaded '
        'to ConPlot, the name chosen for the session and the date in which the session was stored. If you '
        'share a session with another user, all this data will be accessible to the other user, and '
        'it will be displayed together with your username. All this information is visible by members of the '
        'ConPlot team, however it will only be used for development purposes as we will not publicly '
        'release this information or share it with any third parties.', style={"text-align": "justify"})


def GdprPolicySectionFour():
    return html.P(
        'The header on each ConPlot site includes a “Get in Touch” link to a form where users can '
        'submit general inquiries, bug reports or request assistance if they forget their passwords. '
        'Submissions through this form are emailed to members of the Rigden Lab at the University of '
        'Liverpool. The form includes a field for an email address. If the email address identifies you '
        'personally, say if you use your institutional email, then your correspondence with us will '
        'likewise be linked to you. A valid email is not strictly required, although we cannot reply to '
        'you without one. When you submit the form, your IP address and browser version will be '
        'recorded for internal use. In the case of reported bugs or other site errors, this '
        'information may be used by technical staff to help locate your session in the server logs to '
        'aid in troubleshooting the issue. This does have the side effect of making it possible to '
        'associate an IP address with an email address which may, in turn, personally identify you. '
        'However, ConPlot does not publicly release this information.',
        style={"text-align": "justify"})


def GdprPolicySectionFive():
    return html.P(
        'ConPlot uses cookies to associate multiple requests by your web browser into a stateful '
        'session. Cookies are essential to track the state of session. Some cookies persist only for a '
        'single session. The information is recorded temporarily and is erased when the user quits the '
        'session or closes the browser. Others may be persistently stored on the hard drive of your '
        'computer until you manually delete them from a browser folder or until they expire, which can '
        'be months after they were last used. Cookies can be disabled in your browser (refer to your '
        'browser’s documentation for instructions); however, the majority of the website functionality '
        'will be unavailable if cookies are disabled.', style={"text-align": "justify"})


def GdprPolicySectionSix():
    return html.P([
        'If you wish to know more about your rights under the General Data Protection Regulation '
        '(GDPR), you can do this ', html.A(html.U('here'), href=UrlIndex.GDPR_WEBSITE.value),
        '. Here is a summary of what this includes:'], style={"text-align": "left"})

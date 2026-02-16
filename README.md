
<h2>✝️ Cross-Verse Generator</h2>
<p align="center">
<img src="Website/static/cross-icon.png" alt="Cross Verse Logo" width="100%" height="80%">



<i>"Thy word is a lamp unto my feet, and a light unto my path."</i>
  <p style="text-align: center;"><a href =https://cross-verse-generator.onrender.com/><u>View Live Demo</u></a></p>
</p>

<h2>📖 Overview</h2>
<strong>Cross-Verse-Generator</strong> is a Flask-powered web application designed to deliver daily inspiration through randomized scripture.
Built with a focus on clean UI and seamless performance, it provides users with a direct connection to spiritual text through a modern interface.

<h2>📦 Technologies</h2>
<ul>
  <li><strong>Backend</strong>: Python 3 with Flask Framework</li>
  <li><strong>Frontend</strong>: HTML5 (Jinja2 Templates), CSS3, and JavaScript</li>
  <li><strong>Database</strong>: MySQL (Flask-MySQL integration)</li>
  <li><strong>Deployment</strong>: Render (Web Service)</li>
  <li><strong>Server</strong>: Gunicorn (WSGI HTTP Server)</li>
</ul>

<h2>✨  Features</h2>
<ul>
  <li>
    <strong>Contextual Verse Mapping:</strong> Unlike a standard random generator, this app uses a mapping system (<code>mood_aliases</code>) to understand various inputs like "anxious," "stressed," or "blue" and provide a relevant theological response.
  </li>
  <li>
    <strong>Dual-Logic Engine:</strong>
    <ul>
      <li><strong>Specific Search:</strong> Fetches verses tied to specific categories like Depression, Poverty, Fear, Joy, Loneliness, and Tiredness.</li>
      <li><strong>Randomized Discovery:</strong> Provides general inspiration if no specific mood is entered via the <code>/get-random-verse</code> endpoint.</li>
    </ul>
  </li>
  <li>
    <strong>Interactive UI:</strong> A sleek, full-black interface centered around a high-contrast Cross icon that acts as the primary interactive trigger.
  </li>
  <li>
    <strong>Real-Time Updates:</strong> Utilizes the JavaScript <code>fetch</code> API to update the DOM with new scripture without requiring a full page refresh.
  </li>
  <li>
    <strong>Responsive Styling:</strong> Custom CSS ensures a mobile-first, centered layout using Flexbox for accessibility across all devices.
  </li>
</ul>

<h2>⌨️  Navigation</h2>
<ul>
  <li><strong>Prompt Input:</strong> Enter your current situation or emotion (e.g., "sad," "joy") to find tailored scripture.</li>
  <li><strong>The Interactive Cross:</strong> Click the central Cross icon to trigger the <code>get-verse-for-situation</code> logic.</li>
  <li><strong>Dynamic Verse Display:</strong> View your result instantly in the highlighted result area without page reloads.</li>
</ul>

<h2>💡 Project Motivation</h2>
<p>
  This project was built with a dual purpose. On a technical level, I embarked on this to solidify my understanding of the "Full Stack" flow: specifically how <strong>Flask routing</strong> handles complex logic like mood-aliasing and how <strong>asynchronous JavaScript (Fetch API)</strong> creates a seamless, app-like experience.
</p>
<p>
  On a personal level, this app is a reflection of my identity as a Christian. I wanted to build a "real-world" tool that wasn't just a coding exercise, but something that actually serves a purpose in my daily walk. By combining my passion for Computer Science with my faith, I created a digital space where technology acts as a bridge to spiritual encouragement—providing the right word exactly when it's needed most.
</p>

<h2>📫 Contact</h2>
<ul>
  <li><strong>John Sang</strong> - johnsang1970@gmail.com</li>
  <li><strong>Project Link</strong>: https://github.com/johnsang16/Cross-Verse-Generator/</li>
</ul>

<h2>🤝 Acknowledgements</h2>
Special Thanks to:
<ul>
  <li>
    <a href:https://www.flaticon.com/free-icons/cross><strong>Flaticon</strong> :</a>Special thanks to <em>Freepik</em> for the high-quality Cross icon that serves as the visual and interactive anchor of the site.
  </li>
  <li>
    <a href:https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world><strong>Miguel Grinberg's </strong>:</a> Whose <em>Flask Mega-Tutorial</em> served as the foundational roadmap for mastering routing, templates, and the deployment of this web service.
  </li>
  <li>
    <a href:https://bible.com>The Bible App</strong>: Providing scripture for this app's verses and being an accesible free program for Christian's around the world</a>
  </li>
</ul>

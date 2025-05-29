<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Horizontal Scrolling Text</title>
  <style>
    .scrolling-text {
      font-size: 24px;
      font-weight: bold;
      white-space: nowrap;
    }
  </style>
</head>
<body>
  <!-- The marquee tag creates the scrolling effect.
       onmouseover stops the scroll when the mouse hovers over it,
       onmouseout resumes the scrolling. -->
  <marquee behavior="scroll" direction="left" scrollamount="5"
           onmouseover="this.stop();" onmouseout="this.start();"
           class="scrolling-text">
    <span style="color: red;">ADMISSIONS OPEN (2025 - 2026)</span>
    <span style="color: blue;"> FOR UG, PG & Ph.D PROGRAMMES</span>
    <span style="color: green;"> IN SIMATS ENGINEERING</span>
    <span style="color: orange;"> FOR MORE DETAILS</span>
    <span style="color: purple;"> VISIT</span>
    <a href="https://simatsadmissions.saveetha.com/" style="color: magenta; text-decoration: none;"> text!</a>
  </marquee>
</body>
</html>


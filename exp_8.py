<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>  </title>
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
    <span style="color: red;">ADMISSIONS OPEN</span>
    <span style="color: blue;"> FOR UG, PG & Ph.D PROGRAMMES</span>
    <span style="color: green;"> IN SIMATS ENGINEERING</span>
    <span style="color: orange;"> colorful</span>
    <span style="color: purple;"> scrolling</span>
    <span style="color: magenta;"> text!</span>
  </marquee>
</body>
</html>
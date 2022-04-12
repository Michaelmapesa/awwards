const projects = document.querySelector(".projects");

// Loop and in each iteration render an image randomly
// step maxValue is the numbers of images to render
for (let step = 0; step < 8; step++) {
  let imgInd = Math.floor(Math.random() * 12) + 1;

  const projectHTML = `
  <div class="project">
    <div class="project__bg">
        <img src="static/img/gal-${imgInd}.jpg" alt="Project image"
            class="project__img">
    </div>
    <div class="project__info">
        <h2 class="project__title">title</h2>
        <p class="project__description">description</p>
        <span class="project__footer">
            <img src="static/img/gal-${imgInd}.jpg" alt="User img">
            <p>By David Kiama</p>
        </span>
    </div>
    </div>
    
    `;
  projects.insertAdjacentHTML("beforeend", projectHTML);
}
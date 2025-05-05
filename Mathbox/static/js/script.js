document.addEventListener('DOMContentLoaded', function() {
    const kids = document.getElementById("kids");
    const students = document.getElementById("students");
    const left = document.getElementById("left");
    const right = document.getElementById("right");
    const gameInput = document.getElementById("gameSearch");
    const exerciseInput = document.getElementById("exerciseSearch");
    const toolInput = document.getElementById("toolsSearch");
    const communityInput = document.getElementById("communitySearch");
    const docInput = document.getElementById("docSearch");


    if(gameInput) {
        gameInput.addEventListener('input', function(e) {
            const searchTerm = e.target.value.toLowerCase().trim();
            const container = document.getElementById('gamesContainer');
            const cards = Array.from(document.querySelectorAll('.game-card'));
            
            // Find matches and non-matches
            const matches = cards.filter(card => 
              card.dataset.name.includes(searchTerm)
            );
            const nonMatches = cards.filter(card => 
              !card.dataset.name.includes(searchTerm)
            );
          
            // Clear container
            container.innerHTML = '';
          
            // Re-insert cards: matches first, then non-matches
            [...matches, ...nonMatches].forEach(card => {
              container.appendChild(card);
            });
        });
    }
    if(exerciseInput) {
        exerciseInput.addEventListener('input', function(e) {
            const searchTerm = e.target.value.toLowerCase().trim();
            const container = document.getElementById('exerciseContainer');
            const cards = Array.from(document.querySelectorAll('.exercise-card'));
            
            // Find matches and non-matches
            const matches = cards.filter(card => 
              card.dataset.name.includes(searchTerm)
            );
            const nonMatches = cards.filter(card => 
              !card.dataset.name.includes(searchTerm)
            );
          
            // Clear container
            container.innerHTML = '';
          
            // Re-insert cards: matches first, then non-matches
            [...matches, ...nonMatches].forEach(card => {
              container.appendChild(card);
            });
        });
    }
    if(toolInput) {
        toolInput.addEventListener('input', function(e) {
            const searchTerm = e.target.value.toLowerCase().trim();
            const container = document.getElementById('toolsContainer');
            const cards = Array.from(document.querySelectorAll('.tool-card'));
            
            // Find matches and non-matches
            const matches = cards.filter(card => 
              card.dataset.name.includes(searchTerm)
            );
            const nonMatches = cards.filter(card => 
              !card.dataset.name.includes(searchTerm)
            );
          
            // Clear container
            container.innerHTML = '';
          
            // Re-insert cards: matches first, then non-matches
            [...matches, ...nonMatches].forEach(card => {
              container.appendChild(card);
            });
        });
    }
    if(communityInput) {
        communityInput.addEventListener('input', function(e) {
            const searchTerm = e.target.value.toLowerCase().trim();
            const container = document.getElementById('posts');
            const cards = Array.from(document.querySelectorAll('.community-card'));
            
            // Find matches and non-matches
            const matches = cards.filter(card => 
              card.dataset.name.includes(searchTerm)
            );
            const nonMatches = cards.filter(card => 
              !card.dataset.name.includes(searchTerm)
            );
          
            // Clear container
            container.innerHTML = '';
          
            // Re-insert cards: matches first, then non-matches
            [...matches, ...nonMatches].forEach(card => {
              container.appendChild(card);
            });
        });
    }
    if(docInput) {
        docInput.addEventListener('input', function(e) {
            const searchTerm = e.target.value.toLowerCase().trim();
            const left = document.getElementById('left');
            const kidsCard = Array.from(document.querySelectorAll('.kids-card'));
            const right = document.getElementById('right');
            const studentsCard = Array.from(document.querySelectorAll('.students-card'));
            
            // Find matches and non-matches
            const matches = kidsCard.filter(card =>   
              card.dataset.item.includes(searchTerm)
            );
            const nonMatches = kidsCard.filter(card =>   
              !card.dataset.item.includes(searchTerm)
            );
            const matche = studentsCard.filter(cards =>
                cards.dataset.item.includes(searchTerm)
            );
            const nonMatche = studentsCard.filter(cards =>
                !cards.dataset.item.includes(searchTerm)
            );
          
            left.innerHTML = '';
            right.innerHTML = '';
          
            [...matches, ...nonMatches].forEach(card => {
              left.appendChild(card);
            });
            [...matche, ...nonMatche].forEach(cards => {
                right.appendChild(cards);
            });
        });
    }

    if(students) {
        students.addEventListener(("click"), function() {
            students.style.cssText = "filter: none;width: 100%;text-align: center;background: teal;margin: 0px;padding: 9px;"
            kids.style.cssText = "width: 100%;text-align: center;margin: 0px;background: rgb(55, 155, 155);padding: 9px;filter: blur(1.5px) brightness(100%);"
            left.style.display = "none"
            right.style.display = "block"
            kids.addEventListener(("click"), function() {
                students.style.cssText = "width: 100%;text-align: center;margin: 0px;background: rgb(55, 155, 155);padding: 9px;filter: blur(1.5px) brightness(100%);"
                kids.style.cssText = "filter: none;width: 100%;text-align: center;background: teal;margin: 0px;padding: 9px;"
                right.style.display = "none"
                left.style.display = "block"
            });
        });
    }
});
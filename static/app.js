let globalSolutions;

const clearBoard = () => {
    for (let i = 0; i < 16; i++) {
        let id = String(i);
        document.getElementById(id).value = "";
    }
}

const solveBoard = () => {
    const letters = parseLetters();
    const url = window.location.href + '/solutions?letters=' + letters;

    fetch(url)
        .then((response) => { return response.json() })
        .then((data) => { processSolutions(data) })
        .catch((error) => { console.log(error) });
}

const parseLetters = () => {
    let letters = '';

    for (let i = 0; i < 16; i++) {
        let id = String(i);
        letters += document.getElementById(id).value;
    }

    if (letters.length == 16) {
        return letters;
    }
    else {
        alert("make sure to fill in all letters!");
    }
}

const processSolutions = (solutions) => {
    let wordList = new Array();
    globalSolutions = solutions;

    for (wordLength in solutions) {
        for (word in solutions[wordLength])
            wordList.push(word);
    }

    wordList.reverse();
    displaySolutions(wordList);
}

const displaySolutions = (wordList) => {
    wordListHTML = ``;
    maxScore = 0;

    for (word of wordList) {   
        maxScore += calculateWordValue(word);
        wordListHTML += `
        <div class="solution" onmouseover="showWordPath('${word}')" onmouseleave="hideWordPath('${word}')"> 
            ${word} 
        </div>`;
    }

    document.getElementById("statistics").innerHTML = `
        Total Words: ${wordList.length} | Maximum Possible Score: ${maxScore.toLocaleString('en-US')}`;
    document.getElementById("solutions").classList.remove("hidden");
    document.getElementById("solutions").innerHTML = wordListHTML;
}

const calculateWordValue = (word) => {
    if (word.length = 3) {
        return 100;
    }
    else if (word.length >= 4 && word.length <= 5) {
        return 400 * (word.length - 3);
    }
    else {
        return 1400 + (400 * (word.length - 6));
    }
}

const showWordPath = (word) => {
    let wordPath = globalSolutions[word.length][word];
    let colorFactor = 0;
    let color;

    for (pos of wordPath) {
        if (colorFactor == 0) {
            color = `rgb(255,0,0)`
        }
        else {
            color = `rgba(175,0,0)`
        }

        document.getElementById(String(pos)).style.setProperty("background-color", color);
        colorFactor += 50 / word.length;
    }
}

const hideWordPath = (word) => {
    let wordPath = globalSolutions[word.length][word];

    for (pos of wordPath) {
        document.getElementById(String(pos)).style.setProperty("background-color", "#f5c755");
    }
}


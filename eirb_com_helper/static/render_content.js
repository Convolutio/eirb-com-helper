// Script for rendering markdown into HTML in real-time
marked.use({ gfm: true, breaks: true });

// After input, wait 1 sec inactivity before save
const TIME_BEFORE_SAVE = 1000;
let timeoutId = null;

/**
  * @param {string} s 
  */
function toMessageHTML(s) {
	function forceLineBreak(s) {
		// Transform 3+n linebreaks into 3 linebreaks and n+1 <br/> tags 
		// enable this to lengthen the height space between two paragraphs
		const lineBreakPairToLineBreakTag = (s) => s.replace(
			/\n{3,}/g, (match) => (
				"\n" + "<br/>".repeat(match.length-2) +
				"\n\n"
			));
		return s.split("```").map(
			(part, i) => (i%2)?part:lineBreakPairToLineBreakTag(part)
		).join("```");
	}
	function processSpoilers(s) {
		const parts = s.split("||");
		if (parts.length === 1) return s;
		const firstPart = parts.shift();
		const lastPart = parts.pop();
		const res = parts.reduce(
			(acc, part, idx) => acc + (((idx+1)%2)?`<span class="spoiler">${part}</span>`:part),
			firstPart) + lastPart;
		return res;
	}
	function processCheckboxes(s) {
		return s.replace(/\- \[ \]/g, () => "- ⬜")
		.replace(/\- \[x\]/g, () => "- ✅")
	}
	return processCheckboxes(processSpoilers(forceLineBreak(s)));
}


/**
  * Compile markdown to HTML and write it inside renderedContentDiv
  * @param {string} markdownContent
  * @param {HTMLElement} renderedContentDiv
  */
function renderContent(markdownContent, renderedContentDiv) {
  renderedContentDiv.innerHTML = DOMPurify.sanitize(
    marked.parse(toMessageHTML(markdownContent), { sanitize: true })
  );
}


function listenForRender(markdownContentTextArea, renderedContentDiv) {
  markdownContentTextArea.addEventListener('input', () => {
    renderContent(markdownContentTextArea.value, renderedContentDiv);

    // save draft to store
    if (timeoutId !== null)
      clearTimeout(timeoutId);

    timeoutId = setTimeout(() => {
      setDraft(markdownContentTextArea.value);
    }, TIME_BEFORE_SAVE);
  });
}

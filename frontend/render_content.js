// Script for rendering markdown into HTML in real-time
marked.use({ gfm: true, breaks: true });

const markdownContentTextarea = document.getElementById("message");
const renderedContentDiv = document.getElementById('rendered-content');

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
		return parts.reduce(
			(acc, part) => acc + `<span class="spoiler">${part}</span>`,
			firstPart) + lastPart;
	}
	return processSpoilers(forceLineBreak(s));
}

function renderContent() {
	const markdownContent = markdownContentTextarea.value;
	renderedContentDiv.innerHTML = DOMPurify.sanitize(
		marked.parse(toMessageHTML(markdownContent), { sanitize: true })
	);
}

markdownContentTextarea.addEventListener('input', renderContent);

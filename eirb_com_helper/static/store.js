/**
  *  @returns string
  */
function getChatId() {
  const chatId = localStorage.getItem("chatId");
  return chatId ?? "";
}


/**
  *  @param {string} chatId 
  *  @returns void
  */
function setChatId(chatId) {
  localStorage.setItem("chatId", chatId);
}


/**
  *  @param {string} draft 
  *  @returns void
  */
function setDraft(draft) {
  localStorage.setItem("draft", draft);
}


/**
  *  @returns string
  */
function getDraft() {
  const draft = localStorage.getItem("draft");
  return draft ?? "";
}


/**
  * Remove all entries from the store
  */
function clearStore() {
  setChatId("");
  setDraft("");
}


/**
  * Set entries in the store from JSON data
  * @param {{chatId: string;draft: string;}} store 
  */
function loadStore(store) {
  setChatId(store.chatId);
  setDraft(store.draft);
}


/**
  * @returns {{chatId: string;draft: string;}}
  */
function exportStore() {
  return {
    chatId: getChatId(),
    draft: getDraft()
  };
}

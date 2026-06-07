const toggle = document.getElementById('ron-toggle');
const panel  = document.getElementById('ron-panel');
const msgs   = document.getElementById('ron-messages');
const input  = document.getElementById('ron-input');
const send   = document.getElementById('ron-send');

toggle.addEventListener('click', () => panel.classList.toggle('open'));

function addMsg(text, role) {
  const d = document.createElement('div');
  d.className = 'msg ' + role;
  d.textContent = text;
  msgs.appendChild(d);
  msgs.scrollTop = msgs.scrollHeight;
  return d;
}

function showTyping() {
  const d = document.createElement('div');
  d.className = 'msg typing';
  d.innerHTML = '<div class="typing-dots"><span></span><span></span><span></span></div>';
  msgs.appendChild(d);
  msgs.scrollTop = msgs.scrollHeight;
  return d;
}

async function askRon() {
  const q = input.value.trim();
  if (!q) return;
  input.value = '';
  addMsg(q, 'user');
  const typing = showTyping();
  try {
    const res = await fetch('/api/ron/chat/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ question: q })
    });
    const data = await res.json();
    typing.remove();
    addMsg(data.answer || 'Something went wrong.', 'bot');
  } catch {
    typing.remove();
    addMsg('Could not reach RON. Try again.', 'bot');
  }
}

send.addEventListener('click', askRon);
input.addEventListener('keydown', e => { if (e.key === 'Enter') askRon(); });
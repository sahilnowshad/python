# make_todo_page.py
# Creates a simple static todo.html and opens it in your browser.
# Run: python make_todo_page.py

import webbrowser
from pathlib import Path

HTML = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Simple To-Do</title>
<meta name="viewport" content="width=device-width,initial-scale=1">
<style>
  body{font-family:Arial,Helvetica,sans-serif;background:#f4f7fb;padding:30px}
  .card{max-width:540px;margin:0 auto;background:#fff;padding:18px;border-radius:8px;box-shadow:0 6px 18px rgba(0,0,0,0.06)}
  h2{margin:0 0 10px;font-size:20px}
  .row{display:flex;gap:8px}
  input{flex:1;padding:8px;border:1px solid #ddd;border-radius:6px}
  button{padding:8px 10px;border:none;background:#2563eb;color:#fff;border-radius:6px;cursor:pointer}
  ul{list-style:none;padding:0;margin:12px 0}
  li{display:flex;justify-content:space-between;padding:8px 0;border-bottom:1px solid #f0f0f0}
  .del{background:#ef4444;border:none;color:#fff;padding:6px 8px;border-radius:6px;cursor:pointer}
  .muted{color:#666;font-size:13px}
</style>
</head>
<body>
  <div class="card">
    <h2>Simple To-Do</h2>
    <div class="row">
      <input id="task" placeholder="Add a task and press Add or Enter">
      <button id="add">Add</button>
    </div>
    <ul id="list"></ul>
    <div style="display:flex;justify-content:space-between;align-items:center">
      <div class="muted" id="count">0 tasks</div>
      <div>
        <button id="clear" style="background:transparent;color:#2563eb;border:1px solid #e6eefc;padding:6px 8px;border-radius:6px;cursor:pointer">Clear all</button>
      </div>
    </div>
  </div>

<script>
const input = document.getElementById('task');
const addBtn = document.getElementById('add');
const list = document.getElementById('list');
const clearBtn = document.getElementById('clear');
const count = document.getElementById('count');

function load(){ return JSON.parse(localStorage.getItem('todo_tasks')||'[]'); }
function save(t){ localStorage.setItem('todo_tasks', JSON.stringify(t)); }

function render(){
  const tasks = load();
  list.innerHTML = '';
  if(tasks.length===0){
    list.innerHTML = '<li class="muted">No tasks yet</li>';
  } else {
    tasks.forEach((t,i)=>{
      const li = document.createElement('li');
      li.innerHTML = <div><strong>${i+1}.</strong> ${escapeHtml(t)}</div>;
      const d = document.createElement('button');
      d.className='del'; d.textContent='Delete';
      d.onclick = ()=>{ tasks.splice(i,1); save(tasks); render(); };
      li.appendChild(d);
      list.appendChild(li);
    });
  }
  count.textContent = tasks.length + (tasks.length===1?' task':' tasks');
}

function add(){
  const v = input.value.trim();
  if(!v) return input.focus();
  const tasks = load(); tasks.push(v); save(tasks); input.value=''; input.focus(); render();
}

addBtn.onclick = add;
input.addEventListener('keydown', e=>{ if(e.key==='Enter') add(); });
clearBtn.onclick = ()=>{ if(confirm('Remove all tasks?')){ save([]); render(); } };

function escapeHtml(s){ return s.replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;'); }

render();
</script>
</body>
</html>
"""

def main():
    out = Path("todo.html")
    out.write_text(HTML, encoding="utf-8")
    webbrowser.open(out.resolve().as_uri())
    print(f"Created {out.resolve()} and opened it in your browser.")

if __name__ == "__main__":
    main()
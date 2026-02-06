const username = "RiemarSeruelas";
const repo = "Portfolio"; 
const branch = "main";          

const projectsGrid = document.getElementById("projects-grid");

async function fetchRepoContents(path = "") {
  const url = `https://api.github.com/repos/${username}/${repo}/contents/${path}?ref=${branch}`;
  const response = await fetch(url);
  return response.json();
}

function createFileElement(item, path) {
  const fileLink = document.createElement("button");
  fileLink.textContent = item.name;
  fileLink.classList.add("file");

  fileLink.onclick = () => {
    const pageUrl = `https://${username}.github.io/${repo}/${path}${item.name}`;
    window.open(pageUrl, "_blank");
  };

  return fileLink;
}

async function createFolderElement(item) {
  const folderDiv = document.createElement("div");
  folderDiv.classList.add("folder");

  const folderTitle = document.createElement("h4");
  folderTitle.textContent = `📂 ${item.name}`;
  folderDiv.appendChild(folderTitle);

  const folderContents = document.createElement("div");
  folderContents.classList.add("folder-contents");
  folderDiv.appendChild(folderContents);

  const contents = await fetchRepoContents(item.path);

  contents.forEach(child => {
    if (child.type === "file" && child.name.endsWith(".html")) {
      folderContents.appendChild(createFileElement(child, item.path + "/"));
    }
  });

  return folderDiv;
}

async function loadProjects() {
  const rootContents = await fetchRepoContents();

  for (const item of rootContents) {
    if (item.type === "dir") {
      const folderElement = await createFolderElement(item);
      projectsGrid.appendChild(folderElement);
    }
  }
}

loadProjects();
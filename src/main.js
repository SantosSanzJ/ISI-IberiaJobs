function getData() {
    fetch('secrets.json')
      .then(response => response.json())
      .then(json => {
        const apiKey = json.Jooble;
        const url = "https://jooble.org/api/";
        
        const headers = {
          "Content-type": "application/json",
        };
      
        const body = {
          "keywords": "it",
          "location": "Madrid"
        };
      
        fetch(url + apiKey, {
          method: "POST",
          headers: headers,
          body: JSON.stringify(body)
        })
        .then(response => response.json())
        .then(data => {
            const tbody = document.querySelector("#output tbody");
            tbody.innerHTML = "";
            
            data.jobs.forEach(job => {
              const tr = document.createElement("tr");
              const tdCompany = document.createElement("td");
              tdCompany.textContent = job.company;
              tr.appendChild(tdCompany);
              const tdTitle = document.createElement("td");
              tdTitle.textContent = job.title;
              tr.appendChild(tdTitle);
              const tdDescription = document.createElement("td");
              tdDescription.textContent = job.snippet;
              tr.appendChild(tdDescription);
              const tdLocation = document.createElement("td");
              tdLocation.textContent = job.location;
              tr.appendChild(tdLocation);
              tbody.appendChild(tr);
            });
        })
        .catch(error => console.error(error));
      })
      .catch(error => console.error(error));
  }
   
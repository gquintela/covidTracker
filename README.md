# COVID-19 Visualizer and Tracker

Using the <code>corona-api.com</code> API and <code>tkinter</code>, I created a GUI to quickly retrieve information about COVID-19 and display it graphically. Data is temporarilly cached locally so that only one GET request is done per session.

---

## EXAMPLES

![alt text](/data/img/menu1.png)
![alt text](/data/img/menu2.png)
![alt text](/data/img/results.png)

---

You can retrieve information about:

  <ul>
<li>almost any country</li>
<li>up to 180 days before today</li>
<li> get only a particular day (e.g.: last 5 thursdays)</li>
    
<li> choose beetween 
  <ul>
    <li>Deaths</li>
    <li>Confirmed</li>
    <li>Recovered</li>
    <li>New confirmed</li>
    <li>New recovered</li>
    <li>New deaths</li>
    <li>Active</li>  
    </ul>
  </li>
</ul>

  -----
  
  ## USAGE
  
  <code>pip3 install requirements.txt</code>
  
  <code>python3 main.py</code> from <code>src/</code>
  



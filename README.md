# Api-Mapper
A tool to create visualize api endpoints from burpsuite history.

This tool creates a markdown of API endpoints which then can be used to create visual mindmap using https://markmap.js.org/ or https://marketplace.visualstudio.com/items?itemName=gera2ld.markmap-vscode.

# Working and Usage
As of now the script does not create mindmap directly from burpsuite but rather uses xml file. To create this xml file , set your scope in burpsuite then select all (ctrl+a) , right click and save it as an *.xml* format.

Then use command line to create the markdown from the xml file. The resulting markdown can be used [here](https://markmap.js.org/) to create the mindmap.

```
$ python3 api_mapper.py -f burl_history.xml -path /api
```
The `-path` argument sets path for the api.

### Output example
```
#   `api`
##   `v1`
###   `landing_direct`
####   `access_instructions`
#####   `property`
######  GET , `8742.json`
####  GET , `direct_partner_payment_accounts`
####  GET , `earnings`
####   `properties`
#####  GET , `test-screamy`
######  GET , `homes`
####  GET , `properties?page=1`
####  GET , `property_amenities`
###  GET , POST , `leads`
###  GET , POST , `login`
```
<p>Visualised view:</p>
<img src=api_markmap.JPG width=1500px/>

### To-do
 1.Maybe build its burpsuite extension.

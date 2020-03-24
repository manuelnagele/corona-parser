# Covid 19 data scripts

scripts to gather data about covid 19 pandemic

Create Configuration File ```cp sample-config.json config.json```
  ```
  {
      "datasource":{
          "ministerium_url": "https://info.gesundheitsministerium.at/data/",
          "queries":[
              "Geschlechtsverteilung",
              "Altersverteilung",
              "Bezirke",
              "Bundesland",
              "SimpleData"
          ]
      },
      "logging":{
          "write_to_file": true,
          "file_location":"/path/to/log/file/data.json"
      }
  }
  ```

to test output:

  ```
  telegraf --config telegraf-test.conf --test
  ```

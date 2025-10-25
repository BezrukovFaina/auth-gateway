const xml2js = require('xml2js');
const fs = require('fs');

class Parser {
  constructor(filename, callback) {
    this.filename = filename;
    this.callback = callback;
  }

  startParse() {
    fs.readFile(this.filename, 'utf8', (err, data) => {
      if (err) {
        console.error('Error reading file:', err);
        return;
      }
      const parser = new xml2js.Parser();
      parser.parseString(data, (err, result) => {
        if (err) {
          console.error('Error parsing XML:', err);
          return;
        }
        this.callback(result);
      });
    });
  }
}

module.exports = Parser;
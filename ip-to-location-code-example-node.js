const axios = require("axios");

async function getIpInfo() {
  // Set ip address you want to check
  const ip = "67.250.186.196";

  // Set your access key
  const accessKey = "YOUR_ACCESS_KEY";

  //Concat endpoint and params
  const url =
    "https://apiip.net/api/check?ip=" + ip + "&accessKey=" + accessKey;

  // Make a request and store the response
  const response = await axios.get(url);
  const result = response.data;

  // Output the "code" value inside "currency" object
  console.log(result.currency.code);

  // Output entire result
  console.log(result);
}
getIpInfo();

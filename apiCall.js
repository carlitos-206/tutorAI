const indexCall = async(url) =>{
  let response = await fetch('http://127.0.0.1:8000/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      url:url
    })
  }
  )

  let test = await response.json()

  console.log(test)
}

// indexCall('https://www.carlitos-206.xyz/')

indexCall("https://www.khanacademy.org/math/cc-sixth-grade-math/cc-6th-ratios-prop-topic/intro-to-ratios/e/representing-ratios")
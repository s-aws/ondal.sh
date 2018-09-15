// Shondal super.simple get signed url nodejs sdk
// uses credentials from ec2 instance profile recommended way to access
// s3 from an ec2 instance
const AWS = require('aws-sdk')
const s3 = new AWS.S3( {region: 'us-east-1'} ) // region of the bucket
const b = 'bucketname'
const k= 'keyname'
const e = 300
var param = { Bucket: b, Key: k, Expires: e }
url = s3.getSignedUrl('getObject', param, function (err, url) {
	console.log(url)})

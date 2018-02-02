/*
 *     This example fetches the account info of a user and displays the balance.
 *         See https://github.com/jnordberg/dsteem for more info and documentation.
 *         */

// Import the dsteem library
// // You can also import only needed components e.g. import {Client, PrivateKey} from 'dsteem'
// import * as dsteem from 'dsteem'
//
// // Create a new client instance using @gtg's public node
// const client = new dsteem.Client.testnet()
//
// // Default export will be executed in playground when run is pressed
// // You can also run with the hotkey CMD+R (press F1 to see all actions)
// export default async function main() {
//     //const [account] = await client.database.getAccounts(['tiagotest'])
//         //alert(`The balance of @${ account.name } is ${ account.balance }`)
//             //console.log(account) // Open your browser's console to see full output
//
//                 var priv_post_key = dsteem.PrivateKey.fromLogin('tiagotest', 'tiagotest', 'posting')
//
//                     client.broadcast.comment({
//                             author: 'tiagotest',
//                                     title: 'this is the best'
//                                             parent_author: '',
//                                                     parent_permlink: 'test',
//                                                             body: 'this is the body',
//                                                                     permlink: 'this-is-the-best',
//                                                                             json_metadata: ''}, priv_post_key)
//                                                                                     .then(function(result){
//                                                                                                 alert(result)
//                                                                                                             console.log('Included in block: ' + result.block_num)
//                                                                                                                     }, function(error) {
//                                                                                                                                 alert(error)
//                                                                                                                                             console.error(error)
//                                                                                                                                                     })
//                                                                                                                                                     }
//                                                                                                                                                     }}}}

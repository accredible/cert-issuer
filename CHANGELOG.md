# CHANGELOG



## v3.6.0 (2024-03-06)

### Chore

* chore(SemanticRelease): run version before publish ([`4b8e5ac`](https://github.com/blockchain-certificates/cert-issuer/commit/4b8e5ac673d72532f02a6f88cf8809e6a3bac60e))

* chore(CI): debug git and semantic release ([`8478dc9`](https://github.com/blockchain-certificates/cert-issuer/commit/8478dc9fdc13a66f4d63f4dca8a2e1dd8d0eeb5c))

* chore(CI): only trigger build when merged ([`0eb4362`](https://github.com/blockchain-certificates/cert-issuer/commit/0eb4362869947c1db167695a2f2acee2fc34581c))

* chore(CI): re-enable semantic release publish ([`7ad9fd5`](https://github.com/blockchain-certificates/cert-issuer/commit/7ad9fd5a6458f133656ab4f5c1ed5bd094727737))

* chore(Compliance): update compliance status ([`3ed92a0`](https://github.com/blockchain-certificates/cert-issuer/commit/3ed92a049e8ac020ff2008e80106c8a2186e6d5f))

* chore(deps): bump get-func-name from 2.0.0 to 2.0.2

Bumps [get-func-name](https://github.com/chaijs/get-func-name) from 2.0.0 to 2.0.2.
- [Release notes](https://github.com/chaijs/get-func-name/releases)
- [Commits](https://github.com/chaijs/get-func-name/commits/v2.0.2)

---
updated-dependencies:
- dependency-name: get-func-name
  dependency-type: indirect
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`0383454`](https://github.com/blockchain-certificates/cert-issuer/commit/0383454152de92ad8a5db4d30c967dc6c5a4b032))

* chore(deps): bump semver from 5.7.1 to 5.7.2

Bumps [semver](https://github.com/npm/node-semver) from 5.7.1 to 5.7.2.
- [Release notes](https://github.com/npm/node-semver/releases)
- [Changelog](https://github.com/npm/node-semver/blob/v5.7.2/CHANGELOG.md)
- [Commits](https://github.com/npm/node-semver/compare/v5.7.1...v5.7.2)

---
updated-dependencies:
- dependency-name: semver
  dependency-type: indirect
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`18f78a6`](https://github.com/blockchain-certificates/cert-issuer/commit/18f78a6ed19dbf56343264b0fae12076f2ee679f))

### Feature

* feat(CredentialSubject): compare credential subject against credential schema before issuance ([`2618b20`](https://github.com/blockchain-certificates/cert-issuer/commit/2618b20752d2a1da8c40f0e8fe8488083223fc12))

* feat(CredentialSchema): verify credentialSchema property validity ([`77d219b`](https://github.com/blockchain-certificates/cert-issuer/commit/77d219b5437a20ade67ea4343931fa39420f6738))

* feat(DataIntegrityProof): handle contexts for data integrity proof ([`b13182b`](https://github.com/blockchain-certificates/cert-issuer/commit/b13182b6b6b8a07b529f986a2caa11ed177a93ef))

* feat(DataIntegrityProof): handle chained proofs according to DataIntegrityProof spec ([`601a216`](https://github.com/blockchain-certificates/cert-issuer/commit/601a2168ab6b3bc00f73fb58266748d5940c43a6))

* feat(DataIntegrityProof): add id to proof ([`814cede`](https://github.com/blockchain-certificates/cert-issuer/commit/814cede6ef80d6c4e9be417eb2e879431ef92353))

* feat(DataIntegrityProof): convert proof format to data integrity proof ([`5f9215e`](https://github.com/blockchain-certificates/cert-issuer/commit/5f9215ea769f9f54541089286dc67f7bd330679d))

* feat(Vc-V2): bump deeps ([`0c83ef1`](https://github.com/blockchain-certificates/cert-issuer/commit/0c83ef1d74b1df660c24e4a6817cbeeec6ff7081))

* feat(Vc-V2): verify expirationDate/validUntil is set after issuanceDate/validFrom ([`eaf47c8`](https://github.com/blockchain-certificates/cert-issuer/commit/eaf47c8a4f5f320516f329964f2b23716bb4348f))

* feat(Vc-V2): add validFrom/validUntil verification ([`cb41e73`](https://github.com/blockchain-certificates/cert-issuer/commit/cb41e73831e36f1edfe8da91932571072bac4914))

* feat(Vc-V2): prevent having both v1 and v2 vc context defined ([`f46dffa`](https://github.com/blockchain-certificates/cert-issuer/commit/f46dffac072c20d5a925aec2ce56210eb63429ca))

* feat(Vc-V2): allow VC v2 context in cert ([`d942606`](https://github.com/blockchain-certificates/cert-issuer/commit/d9426063d7c5781ec14f6926023838ae04f1dd49))

* feat(Vc-V2): bump cert-schema ([`c70f0b5`](https://github.com/blockchain-certificates/cert-issuer/commit/c70f0b553f8d2c825b7852c1a52135d61d5a8002))

### Fix

* fix(Deps): remove unused dependency ([`94d3f83`](https://github.com/blockchain-certificates/cert-issuer/commit/94d3f839f6ee2581f95aaded7bd47e7c838209df))

### Refactor

* refactor(DataIntegrityProof): remove chainedProof2021 class ([`96c6abe`](https://github.com/blockchain-certificates/cert-issuer/commit/96c6abe1a4dbb8e4471598057a0403e70f0df664))

* refactor(DataIntegrityProof): move responsibility of creating proof object to proof handler ([`4b20423`](https://github.com/blockchain-certificates/cert-issuer/commit/4b20423afc257881c4e1ca84a8e1b87d61820dba))

* refactor(DataIntegrityProof): extract merkle proof 2019 to its own constructor ([`889440b`](https://github.com/blockchain-certificates/cert-issuer/commit/889440b7c2fc605861d46325da14401682db901b))

### Unknown

* Merge pull request #270 from blockchain-certificates/feat/support-credential-schema

chore(SemanticRelease): run version before publish ([`c0e2738`](https://github.com/blockchain-certificates/cert-issuer/commit/c0e2738f415c1f333412888eef7a67c761116d44))

* Merge pull request #269 from blockchain-certificates/feat/support-credential-schema

chore(CI): re-enable semantic release publish ([`8d0b7c2`](https://github.com/blockchain-certificates/cert-issuer/commit/8d0b7c2ba6e07a48dc1cc4e4747c717bf76bb572))

* Merge pull request #268 from blockchain-certificates/feat/support-credential-schema

Feat/support credential schema ([`efc311d`](https://github.com/blockchain-certificates/cert-issuer/commit/efc311d1cebbf1583e285c896cac253b013cc011))

* Merge pull request #266 from blockchain-certificates/feat/follow-data-integrity-proof

Feat/follow data integrity proof ([`71adf6c`](https://github.com/blockchain-certificates/cert-issuer/commit/71adf6ceecbed3c2dc785665cc4dcbd2a5ff5277))

* Merge branch &#39;master&#39; of https://github.com/blockchain-certificates/cert-issuer into feat/follow-data-integrity-proof ([`3dc65ff`](https://github.com/blockchain-certificates/cert-issuer/commit/3dc65ffc4258e57323fbe191c761f4e1dc4db9e0))

* Merge pull request #265 from blockchain-certificates/feat/vc-v2-validFrom-validUntil

Feat/vc v2 valid from valid until ([`19a2fc3`](https://github.com/blockchain-certificates/cert-issuer/commit/19a2fc3e43dd1d7a8fa41ff00e37ee7bc98dcd0c))

* Merge pull request #263 from blockchain-certificates/dependabot/npm_and_yarn/get-func-name-2.0.2

chore(deps): bump get-func-name from 2.0.0 to 2.0.2 ([`41c4550`](https://github.com/blockchain-certificates/cert-issuer/commit/41c45500587dbdbc32c590552fe1af23082bd582))

* Merge pull request #264 from blockchain-certificates/fix/update-deps

fix(Deps): remove unused dependency ([`6df70eb`](https://github.com/blockchain-certificates/cert-issuer/commit/6df70eb2fb3b971f1618911a72e7044e115c9757))

* Merge pull request #258 from blockchain-certificates/dependabot/npm_and_yarn/semver-5.7.2

chore(deps): bump semver from 5.7.1 to 5.7.2 ([`d8d36f5`](https://github.com/blockchain-certificates/cert-issuer/commit/d8d36f5e207dee130ed2e08858b2f80ab919d992))


## v3.5.0 (2023-06-07)

### Chore

* chore(Compliance): update compliance status ([`acfd4b7`](https://github.com/blockchain-certificates/cert-issuer/commit/acfd4b73cda3d766daf2087bc91aef65a310d7d2))

* chore(CI): revert run on PR branch ([`65f4150`](https://github.com/blockchain-certificates/cert-issuer/commit/65f4150ee5b3bbb2001e426fb290ce542d4b6503))

* chore(Compliance): publish compliance report on blockcerts.org ([`4506058`](https://github.com/blockchain-certificates/cert-issuer/commit/450605860f7d7fdad5faa91399a6b247c94cc81c))

* chore(Compliance): run publish report only on PR ([`5d83c48`](https://github.com/blockchain-certificates/cert-issuer/commit/5d83c48675dfbf7e34c8fc5e160af5610bc61221))

### Unknown

* Merge pull request #256 from blockchain-certificates/feat/multiple-signatures-non-chained

Support non chained signatures ([`b4d939e`](https://github.com/blockchain-certificates/cert-issuer/commit/b4d939e9a3546bd1e762be17b7a71831aaeb77ad))

* Revert &#34;feat(ConcurrentProofs): chain sign concurrent proofs with merkle root of previous proofs&#34;

This reverts commit 8449a9bc8798ce29759e5c1ba95d1919b0ae9a64. ([`1ecd92f`](https://github.com/blockchain-certificates/cert-issuer/commit/1ecd92f5b895ba2f4f6ad9570ae85b41b46d40b7))

* Merge branch &#39;master&#39; of https://github.com/blockchain-certificates/cert-issuer into feat/concurrent-signatures ([`3461408`](https://github.com/blockchain-certificates/cert-issuer/commit/3461408df9556405683c0d3fc4674a871c61e095))

* Merge pull request #255 from blockchain-certificates/test/vc-compliance

chore(Compliance): publish compliance report on blockcerts.org ([`45dd96c`](https://github.com/blockchain-certificates/cert-issuer/commit/45dd96c7e6e86070257a41b4b7231eed4860f2b1))

* Merge pull request #254 from blockchain-certificates/test/vc-compliance

chore(Compliance): run publish report only on PR ([`9fde14f`](https://github.com/blockchain-certificates/cert-issuer/commit/9fde14fe9e85b1d74f3105444617b8571e351166))


## v3.4.0 (2023-05-26)

### Chore

* chore(Compliance): run publish only on PR ([`1413e52`](https://github.com/blockchain-certificates/cert-issuer/commit/1413e52e5cdbf8992e3c7df8ff1163861ac40e07))

* chore(CI): only build master ([`8941ab6`](https://github.com/blockchain-certificates/cert-issuer/commit/8941ab6f7bd5cb019a77a9e4fec71515010365d9))

* chore(CI): only run on master branch ([`65d50b3`](https://github.com/blockchain-certificates/cert-issuer/commit/65d50b3949189faf84624c552d4ad49578ceb996))

* chore(Compliance): update compliance report ([`3b3eeee`](https://github.com/blockchain-certificates/cert-issuer/commit/3b3eeee67ade61ac2c96ab735653eda4a3cfefdc))

* chore(CI): fix typo ([`102bad4`](https://github.com/blockchain-certificates/cert-issuer/commit/102bad40e0ad8cbee9f5a3854d15ac5253380aa8))

* chore(CI): fix typo ([`8e79505`](https://github.com/blockchain-certificates/cert-issuer/commit/8e795050647972a2c1e727972455e67825ff5b56))

* chore(CI): debug CI ([`1e4acae`](https://github.com/blockchain-certificates/cert-issuer/commit/1e4acae1f72c1d11b4b27438687129199c3b011c))

* chore(CI): debug CI ([`369592c`](https://github.com/blockchain-certificates/cert-issuer/commit/369592cb5a5fc189f5783725f8261871d6a3c25c))

* chore(CI): debug CI ([`621fb1a`](https://github.com/blockchain-certificates/cert-issuer/commit/621fb1a67beda9ff9e45b58942344df085083532))

* chore(Compliance): update compliance report ([`fbd8f67`](https://github.com/blockchain-certificates/cert-issuer/commit/fbd8f67ca0c4e32472b578f92b62be0f56accd3b))

* chore(Compliance): fix badge color ([`9ae1083`](https://github.com/blockchain-certificates/cert-issuer/commit/9ae1083a5adc96c39f1a43b858de98d49a758552))

* chore(Compliance): only run on master branch ([`12fb64a`](https://github.com/blockchain-certificates/cert-issuer/commit/12fb64ae84b3508050e673197ae5810ac6d860a7))

* chore(Compliance): update compliance report ([`c231ed8`](https://github.com/blockchain-certificates/cert-issuer/commit/c231ed8920ef581fb7d8b7c4285318079210b8f0))

* chore(Compliance): update first line of README with latest badge status ([`55b34b8`](https://github.com/blockchain-certificates/cert-issuer/commit/55b34b875691f533bd4ad4ce87ee197bf43dc81a))

* chore(Compliance): create badge and populate readme with status (tentative) ([`13c58c7`](https://github.com/blockchain-certificates/cert-issuer/commit/13c58c768ca64c2b119255e04eeeb6ca94038912))

* chore(Compliance): only run report update on master branch. Ignore compliance private key ([`0e951cd`](https://github.com/blockchain-certificates/cert-issuer/commit/0e951cd2b80914e8f1d77c6f8d3c1901a2337045))

* chore(Compliance): update compliance report ([`8f3e111`](https://github.com/blockchain-certificates/cert-issuer/commit/8f3e11176b26fdde57b1aa1cb623cbd382a2854d))

* chore(Compliance): match target head ([`1a1a4fd`](https://github.com/blockchain-certificates/cert-issuer/commit/1a1a4fd38944d326fe23039660222ad498dcc7c9))

* chore(Compliance): debug commit content ([`e8115d4`](https://github.com/blockchain-certificates/cert-issuer/commit/e8115d47f13d8f054e308e377641ff41956b7554))

* chore(Compliance): attempt Github auth ([`e1f8959`](https://github.com/blockchain-certificates/cert-issuer/commit/e1f8959e48a9401b49f075f1445a75a59b5046ca))

* chore(CI): debug ([`28f5824`](https://github.com/blockchain-certificates/cert-issuer/commit/28f58241f228715a9d817ba66d9c32075f444589))

* chore(Compliance): dwbug CI ([`c2f5e16`](https://github.com/blockchain-certificates/cert-issuer/commit/c2f5e16d29c60d84217accc9b69bb2a2f3a7df7f))

* chore(Compliance): copy report file and commit to repo ([`bc268ca`](https://github.com/blockchain-certificates/cert-issuer/commit/bc268caf59bd7e29bf68a56d828d44e8d5ce4d31))

* chore(Compliance): bump version ([`927c5a0`](https://github.com/blockchain-certificates/cert-issuer/commit/927c5a0064b78a0c86ec87a71d5619416db7dbeb))

* chore(compliance): bump version ([`22ecf45`](https://github.com/blockchain-certificates/cert-issuer/commit/22ecf4585dbd6354bc3880f1e2835c160df7a996))

* chore(Compliance): bump version ([`ae46d7f`](https://github.com/blockchain-certificates/cert-issuer/commit/ae46d7f60fa64334a2006993d7a9ffdce2854bcc))

* chore(Compliance): bump version ([`95f5846`](https://github.com/blockchain-certificates/cert-issuer/commit/95f5846ab5777c0fa3036791d5dc8e991c20f6ee))

* chore(Compliance): bump version ([`158f41c`](https://github.com/blockchain-certificates/cert-issuer/commit/158f41c4e4baee1811015968971822ac3c602b46))

* chore(Compliance): reduce log output ([`2b2a63c`](https://github.com/blockchain-certificates/cert-issuer/commit/2b2a63c42371fa0c3baf844dcdec99b20699ccc2))

* chore(Compliance): bump version ([`160f800`](https://github.com/blockchain-certificates/cert-issuer/commit/160f80042e2271cb40adc6ad85ceed63feb40fa8))

* chore(Compliance): enable compliance run ([`18e08e6`](https://github.com/blockchain-certificates/cert-issuer/commit/18e08e6551cb88ba7bb37201e6eaeaf5994ab2e5))

* chore(Compliance): use simpler example for debug ([`31d98c8`](https://github.com/blockchain-certificates/cert-issuer/commit/31d98c84b41cbab36a97a25d27ed8999d21387ba))

* chore(Compliance): debug ([`65848b7`](https://github.com/blockchain-certificates/cert-issuer/commit/65848b79f34412a2144325a1c9a7eab9bd6b7cfe))

* chore(CI): downgrade python version - 3.11 not working ([`0137b07`](https://github.com/blockchain-certificates/cert-issuer/commit/0137b0772f24befca631a5a35faed6746ab29faf))

* chore(CI): bump python version ([`1901f70`](https://github.com/blockchain-certificates/cert-issuer/commit/1901f7065da39bab0c5552bcc31498e3039e83d9))

### Documentation

* docs(Example): update example cert ([`59f55f9`](https://github.com/blockchain-certificates/cert-issuer/commit/59f55f917e78eb3857372c4d1be71253d2c59b04))

### Feature

* feat(Compliance): throw if issuer is an array ([`02616cc`](https://github.com/blockchain-certificates/cert-issuer/commit/02616ccbf665fe80fcf4c77520ebd92e457444b9))

* feat(StatusList): support issuance of array credentialStatus property value ([`71cabce`](https://github.com/blockchain-certificates/cert-issuer/commit/71cabce20191dc5b56279c00adcc7831fd89ca1f))

* feat(ConcurrentProofs): chain sign concurrent proofs with merkle root of previous proofs ([`8449a9b`](https://github.com/blockchain-certificates/cert-issuer/commit/8449a9bc8798ce29759e5c1ba95d1919b0ae9a64))

* feat(ConcurrentProofs): allow setting nature of multiple proofs by config/CLI ([`6ebf7f1`](https://github.com/blockchain-certificates/cert-issuer/commit/6ebf7f142105d5373d356cdce2d3be33310a2041))

* feat(ProofHandler): add concurrent proof ([`8670875`](https://github.com/blockchain-certificates/cert-issuer/commit/867087522e20774aa8f2301ec89808207a544c2b))

### Fix

* fix(Compliance): improve issuer validation ([`d023dc0`](https://github.com/blockchain-certificates/cert-issuer/commit/d023dc0eb18c2c8958583ce9045fd890e72e4a02))

### Refactor

* refactor(ProofHandler): add chained flag ([`29f91bb`](https://github.com/blockchain-certificates/cert-issuer/commit/29f91bb2a6cf3786c0e026f13c96b4a593fe9f15))

### Unknown

* Merge pull request #251 from blockchain-certificates/test/vc-compliance

Test/vc compliance ([`9133b17`](https://github.com/blockchain-certificates/cert-issuer/commit/9133b17b42053efd91b768547caa9fed22f70ad2))

* Merge branch &#39;test/vc-compliance&#39; of https://github.com/blockchain-certificates/cert-issuer into test/vc-compliance ([`368f1b0`](https://github.com/blockchain-certificates/cert-issuer/commit/368f1b0ae17045fc99c2270d4080d3af178c624a))

* Merge branch &#39;test/vc-compliance&#39; of https://github.com/blockchain-certificates/cert-issuer into test/vc-compliance ([`434334c`](https://github.com/blockchain-certificates/cert-issuer/commit/434334ce9bab8a33cbf7bd19248b34b9b4b039fe))

* Merge branch &#39;test/vc-compliance&#39; of https://github.com/blockchain-certificates/cert-issuer into test/vc-compliance ([`810350e`](https://github.com/blockchain-certificates/cert-issuer/commit/810350e073df6deaded20e45f602f1343f91de2b))

* Merge branch &#39;test/vc-compliance&#39; of https://github.com/blockchain-certificates/cert-issuer into test/vc-compliance ([`5c67a2a`](https://github.com/blockchain-certificates/cert-issuer/commit/5c67a2a35ceddc17431544be3c3c89b7228dac92))

* Merge pull request #239 from digit-ink/master

Enable EIP-1559 ETH txs and update deprecated web3 methods/packages ([`48420fa`](https://github.com/blockchain-certificates/cert-issuer/commit/48420face863658f9412472ce2ce8e823b345581))

* Merge pull request #253 from blockchain-certificates/feat/status-list-2021

feat(StatusList): support issuance of array credentialStatus property… ([`a34a9ac`](https://github.com/blockchain-certificates/cert-issuer/commit/a34a9acefd24b38ddd324530e548a1ea47949f0c))

* Merge pull request #248 from dallarosa/dallarosa-fix-dockerfile-regtest

fix Dockerfile ([`2414aa2`](https://github.com/blockchain-certificates/cert-issuer/commit/2414aa2758148b32a4cedcee702d14c58b7bce14))

* fix Dockerfile

Added the header [regtest] to bitcoin.conf, fixing the error:
&#34;Error: Config setting for -rpcport only applied on regtest network when in [regtest] section.&#34; ([`c528638`](https://github.com/blockchain-certificates/cert-issuer/commit/c5286388d9bc09ebec4e9119323f8dc0c55f00ce))


## v3.3.0 (2022-08-25)

### Chore

* chore(CI): enable semantic release for real ([`ed3d51b`](https://github.com/blockchain-certificates/cert-issuer/commit/ed3d51b72a0c361e739ddaee9c5c9c8fc41f2039))

* chore(CI): configure semantic release to pick up version from tag ([`1e2873f`](https://github.com/blockchain-certificates/cert-issuer/commit/1e2873f7b76cc991c635869948df2cc5906c62b7))

* chore(CI): configure git user ([`5b6c0be`](https://github.com/blockchain-certificates/cert-issuer/commit/5b6c0bef3ac1f5b9f500b811361390c06729e609))

* chore(CI): add debug verbosity ([`ac99779`](https://github.com/blockchain-certificates/cert-issuer/commit/ac99779fb802866641aa93d133b31a8d15d52b95))

* chore(CI): dry-mode for CI configuration ([`6ba2337`](https://github.com/blockchain-certificates/cert-issuer/commit/6ba2337c56ff6710d71a9b14411e4f41e5398a3c))

* chore(SemanticRelease): revert version to 0.0.0 ([`a953103`](https://github.com/blockchain-certificates/cert-issuer/commit/a953103f10bdca2cd3b78bea3e161a5044bc827c))

* chore(CI): break line ([`ae8e823`](https://github.com/blockchain-certificates/cert-issuer/commit/ae8e8231756cc8933f61dfa79a1bb97d88520fb1))

* chore(CI): configure semantic-release ([`9fe0781`](https://github.com/blockchain-certificates/cert-issuer/commit/9fe078189a287a53825268f0ab286f652be65737))

* chore(version): bump version and update dependencies ([`a643fff`](https://github.com/blockchain-certificates/cert-issuer/commit/a643fff114acbb29f2575710a5277e1925cc8a15))

### Documentation

* docs(GoerliAndSepolia): update docs about new supported Ethereum testnets, goerli and sepolia. ([`0355520`](https://github.com/blockchain-certificates/cert-issuer/commit/035552091c469279eca40725e49b6d53c6aae3f1))

### Feature

* feat(GoerliAndSepolia): support Ethereum testnets, goerli and sepolia. ([`a7c3834`](https://github.com/blockchain-certificates/cert-issuer/commit/a7c38345496e1398d097c05751ae72190a297233))

### Refactor

* refactor(GoerliAndSepolia): make it simple using chain.is_bitcoin_type(), is_mock_type(), and is_ethereum_type() ([`fd8785d`](https://github.com/blockchain-certificates/cert-issuer/commit/fd8785d534b7c4178827e0aff6bf5c8907a5c595))

### Unknown

* Merge pull request #245 from blockchain-certificates/chore/semantic-release

chore(CI): enable semantic release for real ([`3d07ec8`](https://github.com/blockchain-certificates/cert-issuer/commit/3d07ec8997aadc9639a02789d841e8d1250cac29))

* Merge pull request #244 from blockchain-certificates/chore/semantic-release

chore(CI): configure semantic release to pick up version from tag ([`3dd6aa8`](https://github.com/blockchain-certificates/cert-issuer/commit/3dd6aa8a3539b321f8863304308f27a75632b052))

* Merge pull request #243 from blockchain-certificates/chore/semantic-release

chore(CI): configure git user ([`ebc4b99`](https://github.com/blockchain-certificates/cert-issuer/commit/ebc4b998279e4a4c76a4bcd4b368db5f8ac7e18a))

* Merge pull request #242 from blockchain-certificates/chore/semantic-release

chore(CI): add debug verbosity ([`d97d5be`](https://github.com/blockchain-certificates/cert-issuer/commit/d97d5be190007bc535a879fb69e4092a6c0de48e))

* Merge pull request #241 from blockchain-certificates/chore/semantic-release

chore(CI): dry-mode for CI configuration ([`66aa531`](https://github.com/blockchain-certificates/cert-issuer/commit/66aa531d22c9f60a8dae5d4ad7ba6ad6de9c660b))

* Merge pull request #240 from blockchain-certificates/chore/semantic-release

chore(CI): configure semantic-release ([`3915889`](https://github.com/blockchain-certificates/cert-issuer/commit/3915889e830f3e607b558589587194edd3c8b98c))

* update UnableToSignTxError() and delete redundant variable ([`107cd83`](https://github.com/blockchain-certificates/cert-issuer/commit/107cd83e9f7e55333673b1cadcee66771f1b0669))

* Enable EIP-1559-compliant ETH transactions and update deprecated web3 methods/packages ([`4f293b3`](https://github.com/blockchain-certificates/cert-issuer/commit/4f293b351127e1e0d791a1d7a44f1a582a90feaa))

* Merge pull request #237 from koshilife/support-goerli-and-sepolia

Support Ethereum testnets, the Goerli and the Sepolia ([`323601a`](https://github.com/blockchain-certificates/cert-issuer/commit/323601a50e5fe111ea03054eef60bebc651a86ec))


## v3.2.0 (2022-07-12)

### Chore

* chore(Package): bump version ([`f7b3543`](https://github.com/blockchain-certificates/cert-issuer/commit/f7b3543d25819aa4706bf7bbafbbf00e8ab293a2))

* chore(MultiSign): ignore context dir ([`adb447e`](https://github.com/blockchain-certificates/cert-issuer/commit/adb447eb81dfb6e362170cc0dbeee5c96962e214))

* chore(MultiSign): do not maintain context in git repo ([`c0478ed`](https://github.com/blockchain-certificates/cert-issuer/commit/c0478ed2a83084ab7dc12103fdaf849b0dc29cd5))

* chore(Release): update release package script ([`55a850a`](https://github.com/blockchain-certificates/cert-issuer/commit/55a850ab5444d10baf57d16591f621355cf9ebdc))

* chore(Tests): remove deprecation warnings ([`12977d7`](https://github.com/blockchain-certificates/cert-issuer/commit/12977d7449e59bf8ce8d9b289b82f1008c01b2b1))

* chore(VC): bump version ([`11c727b`](https://github.com/blockchain-certificates/cert-issuer/commit/11c727b1e71416c1dc8fe30bf63573553b1117d0))

* chore(VC): remove js test scaffholding ([`ad5e454`](https://github.com/blockchain-certificates/cert-issuer/commit/ad5e454af9cdf6b2c85f63c9ce9fd1b803804bd7))

### Documentation

* docs(MultiSign): update readme ([`41eb02d`](https://github.com/blockchain-certificates/cert-issuer/commit/41eb02d1e72f1acee8eb5c2df2518db19174817f))

* docs(v3): update examples ([`cb7b880`](https://github.com/blockchain-certificates/cert-issuer/commit/cb7b8800a8559239703443bd50b0338a2291d33f))

* docs(V3): update documentation ([`7ce5a0a`](https://github.com/blockchain-certificates/cert-issuer/commit/7ce5a0a0bb5eae9f6871f8fd22747342b51a7e01))

* docs(Issuer): update id ([`926d996`](https://github.com/blockchain-certificates/cert-issuer/commit/926d996ec4cdf739d0f5da909938832c99f9673d))

* docs(Issuer): add fixed github URLs ([`f8ca6b9`](https://github.com/blockchain-certificates/cert-issuer/commit/f8ca6b9d13f74936c48476b897b6ae933df2547b))

* docs(Issuer): add sample issuer details ([`06477d0`](https://github.com/blockchain-certificates/cert-issuer/commit/06477d083d0c7a0bcfa1e4480f51242be3977400))

### Feature

* feat(Metadata): check if title property is defined ([`265df12`](https://github.com/blockchain-certificates/cert-issuer/commit/265df1277d8af41430459aeee66faeccdad28c40))

* feat(Metadata): verify metadata when validating certificate ([`fa3fa7e`](https://github.com/blockchain-certificates/cert-issuer/commit/fa3fa7ea207ce3f84a87409521af6ed71e7bb1db))

* feat(Metadata): only warn once when group is not defined ([`53b5e2c`](https://github.com/blockchain-certificates/cert-issuer/commit/53b5e2ccb2bd752a252c5d1aa472f9cf8f116b4a))

* feat(Metadata): check properties existence as defined from display order ([`03b39aa`](https://github.com/blockchain-certificates/cert-issuer/commit/03b39aaedc42bec0afc1aaed9a44873f10afba18))

* feat(Metadata): add metadata json schema validation ([`748985e`](https://github.com/blockchain-certificates/cert-issuer/commit/748985e0939e85bf2636048de775ddba648a47b4))

* feat(MultiSign): allow passing multiple contexts through command line param ([`0f0a3be`](https://github.com/blockchain-certificates/cert-issuer/commit/0f0a3be84576caf46a54dbdf2cefec85ecff1fd5))

* feat(MultiSign): allow passing one context through command line param ([`fb6f1ba`](https://github.com/blockchain-certificates/cert-issuer/commit/fb6f1ba2128c730075a9b15565b637e5f4f189f0))

* feat(MultiSign): register context before issuance ([`d7e1a6b`](https://github.com/blockchain-certificates/cert-issuer/commit/d7e1a6b2a215479d4d25485dcd9f490aec675e97))

* feat(MultiSign): bump version ([`ce82385`](https://github.com/blockchain-certificates/cert-issuer/commit/ce82385c335fc0876b408ce72e5f3bd89b49b584))

* feat(MultiSign): add merkle proof context if document is v3.1 ([`64530ad`](https://github.com/blockchain-certificates/cert-issuer/commit/64530ad44b3325340d9be8faff066b8d98a7eb15))

* feat(MultiSign): update context to reflect signature suites ([`9f75673`](https://github.com/blockchain-certificates/cert-issuer/commit/9f75673584645693192377cc35f77bbe06464bb4))

* feat(MultiSign): bump cert-schema ([`f23cc57`](https://github.com/blockchain-certificates/cert-issuer/commit/f23cc5767fb873edf2302bbd924a05df6b02f365))

* feat(MultiSign): allow n amount of proofs to be chained ([`1c6e3b4`](https://github.com/blockchain-certificates/cert-issuer/commit/1c6e3b4ad8cecc429afddd03a0fb1a9b09687d62))

* feat(V3): provide check to make sure blockcerts context is last ([`18e5396`](https://github.com/blockchain-certificates/cert-issuer/commit/18e539661f04a8f7e9462eb16d7f5eb2bae1979b))

* feat(v3): bump cert-schema dependency ([`8aa3290`](https://github.com/blockchain-certificates/cert-issuer/commit/8aa3290af3d8b79d806d252734efeeae69c2e677))

* feat(v3): bump cert-schema dependency ([`2bdf62d`](https://github.com/blockchain-certificates/cert-issuer/commit/2bdf62d5a744d1f7a3e58ea30a471daebbe99736))

* feat(v3): prepare version ([`34c30dc`](https://github.com/blockchain-certificates/cert-issuer/commit/34c30dc75b7e1ada7fd093f932b875b3e2846cd0))

* feat(Schema): bump cert-schema ([`8b7a1b9`](https://github.com/blockchain-certificates/cert-issuer/commit/8b7a1b96ecd9854d33543bab7cae4035783caa90))

* feat(VerifiableCredential): allow for issuer object with id as per the spec ([`e46702c`](https://github.com/blockchain-certificates/cert-issuer/commit/e46702c40276c1ed51f97c90e692e683f932879d))

* feat(VC): force issuer property to be a URL ([`234df38`](https://github.com/blockchain-certificates/cert-issuer/commit/234df381fadd66afc6ce9265215c3ab232c0cc2b))

* feat(VC): validate @context property ([`a38cb9a`](https://github.com/blockchain-certificates/cert-issuer/commit/a38cb9a0f2652e75d94bbd52c4b0d50f185ff054))

### Fix

* fix(RFC3339): fix regex to differentiate closing group Z or timezone offset ([`41f1797`](https://github.com/blockchain-certificates/cert-issuer/commit/41f1797f6152052d785da16e20837c05abc1cfb1))

* fix(ChainedProof2021): deep copy previous proof to prevent modification by reference ([`0a67cc6`](https://github.com/blockchain-certificates/cert-issuer/commit/0a67cc67c4252a2a9e635092810c602b5b3cb38e))

* fix(Date): allow more valid RFC3339 string values ([`ad7c0b2`](https://github.com/blockchain-certificates/cert-issuer/commit/ad7c0b28ccf3f384bf50acee77f1ca3e96875cd3))

* fix(Context): limit valid context addresses according to cert-schema preloading ([`67693ad`](https://github.com/blockchain-certificates/cert-issuer/commit/67693ad61cfc347af925cc2c6097a15a025aa0f8))

* fix(v3): ensure display is properly hashed ([`f1b1af4`](https://github.com/blockchain-certificates/cert-issuer/commit/f1b1af43ac44906cbe8afa5e1632cf225d488485))

* fix(Etherscan): [#205] prevent captcha request when calling Etherscan ropsten api ([`2998dd6`](https://github.com/blockchain-certificates/cert-issuer/commit/2998dd6a1693ef49c930948a20f00dbf79fdb3ef))

* fix: update new web location of Merkleproof2017

Changing to new location of Merkleproof2017 from https://w3c-dvcg.github.io/lds-merkleproof2017/ to https://w3c-ccg.github.io/lds-merkleproof2017/ ([`4ebe6e2`](https://github.com/blockchain-certificates/cert-issuer/commit/4ebe6e20a27669a9f85ff80cbd1da5beff1459d0))

* fix(Issuance): settle pyld to v1 ([`3fb2477`](https://github.com/blockchain-certificates/cert-issuer/commit/3fb247703d5ce35d11c632e46bcad33e097c39ef))

### Refactor

* refactor(Models): split models file for sanity of the man ([`54bb61a`](https://github.com/blockchain-certificates/cert-issuer/commit/54bb61a552b08162bfec98b44da89082e899a956))

* refactor(JSONLD): centralize jsonld handler ([`f8022b0`](https://github.com/blockchain-certificates/cert-issuer/commit/f8022b079e3a1c79f6b09810855d128ed93bf6be))

* refactor(Proof): abstract proof handler to centralize proof logic ([`4866a3b`](https://github.com/blockchain-certificates/cert-issuer/commit/4866a3b0a0d0b769078354f555d50cc33a3baa0a))

* refactor(Schema): properly instantiate class ([`58bf57e`](https://github.com/blockchain-certificates/cert-issuer/commit/58bf57e6657d188c9bd75e5f311a8e0a8d61bb3e))

* refactor(Schema): use latest cert-schema API ([`bcb534f`](https://github.com/blockchain-certificates/cert-issuer/commit/bcb534f1c9e47f5eaeef18cd9dde7f6cb647383b))

### Style

* style(V3): remove trailing print ([`e83deb5`](https://github.com/blockchain-certificates/cert-issuer/commit/e83deb54e7e4ab31395c628afb1fb4a4fbb243e2))

### Test

* test(Metadata): test issuance check ([`7444fac`](https://github.com/blockchain-certificates/cert-issuer/commit/7444fac3ce187c4340ce726d2970c954619ea763))

* test(Metadata): add tests for displayOrder and schema absence check ([`6601a04`](https://github.com/blockchain-certificates/cert-issuer/commit/6601a04105a2ef9f2fc957228167c40dd2b12a43))

* test(RFC3339): add more test cases ([`cd80945`](https://github.com/blockchain-certificates/cert-issuer/commit/cd80945bc0f6bad9a9c458edfa06773016d8cf66))

* test(V3): test whole VP verification execution ([`2a6026f`](https://github.com/blockchain-certificates/cert-issuer/commit/2a6026f48f8c0a62bc99d4f6a5d4cd96474eb6b2))

* test(V3): test whole VC verification execution ([`ad52583`](https://github.com/blockchain-certificates/cert-issuer/commit/ad52583be48319597c3a0b95cce29a6b7abf788e))

* test(V3): integration test VC compliance passing ([`87ea60c`](https://github.com/blockchain-certificates/cert-issuer/commit/87ea60c36e0ce89d01c8c0c6805bd2e9b1a43a09))

* test(V3): scaffhold integration test VC compliance ([`fdd8104`](https://github.com/blockchain-certificates/cert-issuer/commit/fdd81047a52ae3a93861e4a7b23e9a714b31bb3a))

* test(Validation): add verify_presentation tests ([`8720048`](https://github.com/blockchain-certificates/cert-issuer/commit/872004840cbf8bed355437c58be6ecd55b6a9b92))

* test(Validation): add verify_credential tests ([`86402d6`](https://github.com/blockchain-certificates/cert-issuer/commit/86402d6854a8409859e6abf44e74a0cf364d4df3))

* test(Validation): add validate_credential_status tests ([`d5f7b9c`](https://github.com/blockchain-certificates/cert-issuer/commit/d5f7b9c4d4f22ab89c59627a9b18270c99c5a258))

* test(Validation): add validate_expiration_date tests ([`3142e28`](https://github.com/blockchain-certificates/cert-issuer/commit/3142e2867c615986302913a000a5204e497456e7))

### Unknown

* Merge pull request #238 from blockchain-certificates/feat/validate_metadata

Feat/validate metadata ([`76c99cb`](https://github.com/blockchain-certificates/cert-issuer/commit/76c99cbaa32f06bbec347b6646d605d0f0aac510))

* Merge pull request #232 from blockchain-certificates/poc/proof-chain

Feat: proofChain with chainedProof2021 ([`b268ac4`](https://github.com/blockchain-certificates/cert-issuer/commit/b268ac4b1d54826e7301385120f6a5f1a2634c0c))

* Merge pull request #234 from koshilife/master

Correct the dead link of Merkle Proof Signature Suite 2019 ([`555cd46`](https://github.com/blockchain-certificates/cert-issuer/commit/555cd46b407a272842d08a1a28d5896f01cd1815))

* Correct the dead link of Merkle Proof Signature Suite 2019 ([`60e6c61`](https://github.com/blockchain-certificates/cert-issuer/commit/60e6c6177558029da61a44af31c4336c3fced085))

* Merge pull request #233 from shoito/patch-1

Correct link to DIF universal resolver ([`37f1ac0`](https://github.com/blockchain-certificates/cert-issuer/commit/37f1ac0a94c713ae514dbcf4ee0490e2915b6ab4))

* Correct link to DIF universal resolver ([`959e01c`](https://github.com/blockchain-certificates/cert-issuer/commit/959e01cb8b91a9c0e3162be39e52b56addb385fe))

* Style(CertificateHandler): remove trailing log instructions ([`9ec2260`](https://github.com/blockchain-certificates/cert-issuer/commit/9ec2260563eb6c4138b427423e6d83cfd3cb5910))

* poc(ChainedProof): sign with chainedProof ([`1d2e678`](https://github.com/blockchain-certificates/cert-issuer/commit/1d2e678c9bb63f4a327609fe6376096e5590d153))

* Merge pull request #230 from blockchain-certificates/feat/consume-cert-schema

Feat/consume cert schema ([`b9409a2`](https://github.com/blockchain-certificates/cert-issuer/commit/b9409a2f776664c77a1d9a160d8a7c6e45fb8dda))

* Merge pull request #228 from KhoiUna/readme-fix

fix readme ([`c62268d`](https://github.com/blockchain-certificates/cert-issuer/commit/c62268d749926347e632d290639d5ae695a34167))

* fix readme ([`50aca02`](https://github.com/blockchain-certificates/cert-issuer/commit/50aca028e836c8cee05185ff1dd9bc90798f4465))

* fix readme ([`c5f85ed`](https://github.com/blockchain-certificates/cert-issuer/commit/c5f85ed4a33d6198c71df5c5b4302eb8caad7b03))

* fix readme ([`c3f3bde`](https://github.com/blockchain-certificates/cert-issuer/commit/c3f3bdef3c471a79001d2d1b3141d11b533e55ee))

* fix readme ([`5058990`](https://github.com/blockchain-certificates/cert-issuer/commit/5058990ff01a5c56db683c19644a33006207fe79))

* Merge pull request #226 from KhoiUna/readme-fix

fix README.md: add more detailed instructions ([`33b1394`](https://github.com/blockchain-certificates/cert-issuer/commit/33b13943a6d79353bdc8e3ce0db2330ba174ae92))

* fix readme ([`5afa8e7`](https://github.com/blockchain-certificates/cert-issuer/commit/5afa8e75a1cf617b0a091019bebef540725486fc))

* fix readme ([`b4d0b30`](https://github.com/blockchain-certificates/cert-issuer/commit/b4d0b30fa7321a68d416721d1e19579dbf4d2b53))

* fix readme: bitcoin-cli -generate ([`aada0db`](https://github.com/blockchain-certificates/cert-issuer/commit/aada0db4a19ed4d106b20c34f9c445229790657a))

* fix README.md: add more detailed instructions ([`9b64dd9`](https://github.com/blockchain-certificates/cert-issuer/commit/9b64dd9a997f1739a53bbad3b5b03d15c420ea88))

* fix README.md: add more detailed instructions ([`d83a87d`](https://github.com/blockchain-certificates/cert-issuer/commit/d83a87d6ebf5b7f170749e171a3152de0617828c))

* Merge pull request #225 from KhoiUna/readme-fix

fix readme ([`50bde2a`](https://github.com/blockchain-certificates/cert-issuer/commit/50bde2ae4ba72a0e8d47260638ea635103a8374e))

* fix readme ([`8156b37`](https://github.com/blockchain-certificates/cert-issuer/commit/8156b37d6df398a1a946f59f3e957e899923565f))

* Merge pull request #224 from blockchain-certificates/fix/context-check

fix(Context): limit valid context addresses according to cert-schema preloading ([`a51608a`](https://github.com/blockchain-certificates/cert-issuer/commit/a51608a98033be4fca88df6d3708c98baba2907c))

* Merge pull request #222 from antonellopasella-kedos/patch-1

Move to a more updated image for bitcoind ([`cf8b581`](https://github.com/blockchain-certificates/cert-issuer/commit/cf8b581f7d9fd12c452733b41f12c188f3ba5e66))

* move to a more updated image for bitcoind

this will also support more architectures (like Apple M1 ones) ([`8013e87`](https://github.com/blockchain-certificates/cert-issuer/commit/8013e87039355a196bade71fa2b3690568be0d5c))

* Merge pull request #220 from blockchain-certificates/fix/v3-schema

fix(v3): ensure display is properly hashed ([`e1ea2c6`](https://github.com/blockchain-certificates/cert-issuer/commit/e1ea2c60e5af12884283bdc99160a5795c3783c8))

* Merge pull request #219 from blockchain-certificates/docs/examples

docs(v3): update examples ([`ad37a88`](https://github.com/blockchain-certificates/cert-issuer/commit/ad37a88441c23e327e5ba76c3a5cda60b0b2084c))

* Merge pull request #218 from blockchain-certificates/feat/check-context-order

feat(V3): provide check to make sure blockcerts context is last ([`d267c76`](https://github.com/blockchain-certificates/cert-issuer/commit/d267c7642e9f8ddda7d6d0af9c0439918a2ac4f0))

* Merge pull request #214 from blockchain-certificates/v3

V3 ([`eeb2c1d`](https://github.com/blockchain-certificates/cert-issuer/commit/eeb2c1d7c6b90eb9f09763ee84479b2fe447c0cc))

* Merge branch &#39;v3&#39; of https://github.com/blockchain-certificates/cert-issuer into v3 ([`d888f7d`](https://github.com/blockchain-certificates/cert-issuer/commit/d888f7d5cfc9062ab44ef1e126d6424270069f50))

* Merge branch &#39;master&#39; into v3 ([`db7d026`](https://github.com/blockchain-certificates/cert-issuer/commit/db7d026261f5bb3c8bdcae90bc25122f6148756d))

* Merge pull request #213 from blockchain-certificates/feat/v3-jf-updates

prevent captcha request when calling Etherscan ropsten API ([`99d244d`](https://github.com/blockchain-certificates/cert-issuer/commit/99d244d8fd2afc9f2fc6d2feea10b79d8427ffac))

* Merge branch &#39;v3&#39; of https://github.com/blockchain-certificates/cert-issuer into v3 ([`926c7d1`](https://github.com/blockchain-certificates/cert-issuer/commit/926c7d1b8bfa562ced6cc10fbf03175430ebbba4))

* Merge pull request #212 from Kedos-srl/fix_ropsten_url_changed

Ropsten API URL changed and the normal requests are blocked with a 40… ([`43191df`](https://github.com/blockchain-certificates/cert-issuer/commit/43191df9d8a37e92dbb35af40aec069cdca53475))

* Revving version. ([`510ee37`](https://github.com/blockchain-certificates/cert-issuer/commit/510ee370101a3887d7b7699bd6a62aa05f869948))

* Ropsten API URL changed and the normal requests are blocked with a 403 if the User Agent is python-requests. ([`5a4b7da`](https://github.com/blockchain-certificates/cert-issuer/commit/5a4b7da571f3d70a901a686bc6fb7bd81543fc3f))

* Merge branch &#39;master&#39; into v3 ([`a57249c`](https://github.com/blockchain-certificates/cert-issuer/commit/a57249cee8c03143356c32f4266f0923eee3a15d))

* Merge pull request #208 from blockchain-certificates/fu_bad_dependencies

Fixed bad dependencies in the Dockerfile ([`6b4879a`](https://github.com/blockchain-certificates/cert-issuer/commit/6b4879a8076f468517ab02a58c61041c21df667f))

* #207 - Dealt with some dependency issues that prevented the Docker container from building. ([`73f25fa`](https://github.com/blockchain-certificates/cert-issuer/commit/73f25fa98c26e13351216f1d59cb8a677924b3bf))

* Updated some dependencies.  Let&#39;s hope it works. ([`e733298`](https://github.com/blockchain-certificates/cert-issuer/commit/e7332984b292a40c1b6b9704ddc55c49267be80f))

* #136 - Commented out MyEtherWallet bindings for now. ([`b7d2520`](https://github.com/blockchain-certificates/cert-issuer/commit/b7d252068e565d1323b283cb9d03a202b3b6e64d))

* Merge pull request #202 from blockchain-certificates/docs/sample-issuer

docs(Issuer): add fixed github URLs ([`a7fb942`](https://github.com/blockchain-certificates/cert-issuer/commit/a7fb9421780237cf9becbdafc81b61657ec07142))

* Merge pull request #201 from blockchain-certificates/docs/sample-issuer

docs(Issuer): add sample issuer details ([`eb3f6a2`](https://github.com/blockchain-certificates/cert-issuer/commit/eb3f6a2513af18e07cbe001b696dae627839895c))

* Merge pull request #196 from danishfastian/master

Certissuer fix related to BlockCypher configuration ([`c3c7233`](https://github.com/blockchain-certificates/cert-issuer/commit/c3c723346465d2fb396375217db6cf861808555e))

* Add missing blockcypher_api_token aggument ([`3fed1a4`](https://github.com/blockchain-certificates/cert-issuer/commit/3fed1a4bb79cbb88a6e46f94061bf64e4ba95d41))

* Merge pull request #1 from blockchain-certificates/master

Sync from main repository ([`5f46678`](https://github.com/blockchain-certificates/cert-issuer/commit/5f46678f42b7a9bb1bfb78b225b5e437a93b138f))

* Merge pull request #193 from fuerve/lp-eth-fixes

A positional argument error somehow slipped through. ([`9b0ed45`](https://github.com/blockchain-certificates/cert-issuer/commit/9b0ed451ef686018a507acd8bb7d217263a6fbf4))

* Revving version number. ([`7f1127b`](https://github.com/blockchain-certificates/cert-issuer/commit/7f1127bf224558c91153def5f5532c4d87d34229))

* A positional argument error somehow slipped through. ([`7cfdde6`](https://github.com/blockchain-certificates/cert-issuer/commit/7cfdde603ca23d49205b184d1225b8b9fdab0f95))

* Merge pull request #192 from fuerve/lp-eth-fixes

Adding a connector for Ethereum RPC providers. ([`febeda1`](https://github.com/blockchain-certificates/cert-issuer/commit/febeda11bb024ac9c2cefad23eaf2b5f75804fda))

* Typo ([`a8b5766`](https://github.com/blockchain-certificates/cert-issuer/commit/a8b57667380d9fc70edde793445bde1858f4a9ae))

* Fixup to the Ethereum RPC environment variable name. ([`64ee146`](https://github.com/blockchain-certificates/cert-issuer/commit/64ee146062af016f8018d3b0cf030fd00bf10447))

* Merge branch &#39;lp-eth-fixes&#39; of https://github.com/fuerve/cert-issuer into lp-eth-fixes ([`55671e4`](https://github.com/blockchain-certificates/cert-issuer/commit/55671e467aaad7597b38c5b8c99cdac4d3a77baf))

* Fixup to the Ethereum RPC environment variable name. ([`a170429`](https://github.com/blockchain-certificates/cert-issuer/commit/a17042923d84bb4e24097f684f70180b6cac7782))

* Merge branch &#39;master&#39; into lp-eth-fixes ([`5fefb9c`](https://github.com/blockchain-certificates/cert-issuer/commit/5fefb9c8df6dc8a4f214605c3bd8b3096bb4b8d8))

* Version number fixed.  Oops. ([`fd06237`](https://github.com/blockchain-certificates/cert-issuer/commit/fd06237151ffd2d51fba49a02fe36154e6427770))

* Added a little bit of logging. ([`8759015`](https://github.com/blockchain-certificates/cert-issuer/commit/875901549ce0f20bf2ff7434707af5b48656fab4))

* Fixups for Ethereum RPC connections. ([`680b171`](https://github.com/blockchain-certificates/cert-issuer/commit/680b171244d28c347c2ca585e4e9380f87fbfd56))

* Merge pull request #191 from blockchain-certificates/test/v3-unit-testing

Test/v3 unit testing ([`37399da`](https://github.com/blockchain-certificates/cert-issuer/commit/37399da56508dba073abea0f759b4157d0830cd5))

* Adding a note about v3 Blockcerts to the master README. ([`d9c063a`](https://github.com/blockchain-certificates/cert-issuer/commit/d9c063a5369d21743221dcb80404388584ad122f))

* Revving to version 3.0.0b2 ([`e064c64`](https://github.com/blockchain-certificates/cert-issuer/commit/e064c64970ddf5a02723d5e5ac07a77bfbff1684))

* Merge branch &#39;v3&#39; of https://github.com/blockchain-certificates/cert-issuer into v3 ([`ecad0fb`](https://github.com/blockchain-certificates/cert-issuer/commit/ecad0fb301f60092d9384745db0ea5ce5917f155))

* Revving to 3.0.0b1 ([`0004099`](https://github.com/blockchain-certificates/cert-issuer/commit/0004099fd716d17e16bb4918f5a25c7b63e7d9c7))

* Revving cert-issuer to 2.0.25 ([`def3f66`](https://github.com/blockchain-certificates/cert-issuer/commit/def3f6622bb086b9719a0720857b0e1a7fca7258))

* Merge branch &#39;master&#39; into v3 ([`d261b7b`](https://github.com/blockchain-certificates/cert-issuer/commit/d261b7b9c51b9d374ff4c9ea39d208f21a78d9e5))

* Merge pull request #186 from fuerve/master

Removing Blockexplorer and Bitpay broadcasters, as they no longer work. ([`1506ed4`](https://github.com/blockchain-certificates/cert-issuer/commit/1506ed4b7527ca9f85f651ded7e843839bbc099c))

* Removing Blockexplorer and Bitpay broadcasters, as they no longer work. ([`dd49883`](https://github.com/blockchain-certificates/cert-issuer/commit/dd49883bdafe566fb8cfeb4aa441ddac76f3ce9b))

* Merge branch &#39;lp-eth-fixes&#39; of https://github.com/fuerve/cert-issuer into lp-eth-fixes ([`73fcc0d`](https://github.com/blockchain-certificates/cert-issuer/commit/73fcc0db60429f7d4fcff79de37fb339a84c4fb5))

* Merge pull request #185 from blockchain-certificates/v3-vc-compliance-test

V3 vc compliance test ([`c8f078f`](https://github.com/blockchain-certificates/cert-issuer/commit/c8f078f380fb492e550c49cda4059191f44ebfdf))

* tests(V3): fix tests failure ([`9ec7160`](https://github.com/blockchain-certificates/cert-issuer/commit/9ec7160815263ae578353bd8c7c9f4eabe4840c0))

* Merge pull request #184 from rajvijen/patch-1

fix: update new web location of Merkleproof-2017 ([`8fbd82e`](https://github.com/blockchain-certificates/cert-issuer/commit/8fbd82e75174e7ab0de9cbde1238d1ca0a7a3baf))

* test scaffholding to run local code ([`7703e50`](https://github.com/blockchain-certificates/cert-issuer/commit/7703e50525f019c54a7caa590a1d1e312b91ecd5))

* Adding support for Ethereum RPC. ([`d97309c`](https://github.com/blockchain-certificates/cert-issuer/commit/d97309c57f99d12c53c22f2fcc7e9579a7c2d109))

* Revving version to republish PyPI package. ([`7d03e7f`](https://github.com/blockchain-certificates/cert-issuer/commit/7d03e7fc130b47d865dd05f3f4a47353b3c54c30))

* Merge pull request #175 from blockchain-certificates/docs

Restructuring documentation ([`83221a3`](https://github.com/blockchain-certificates/cert-issuer/commit/83221a38552c3d0e488f416f8cb533a350d89ffa))

* Restructuring documentation ([`a69f2e9`](https://github.com/blockchain-certificates/cert-issuer/commit/a69f2e9643ef3d31c6e7a956adcbf10194e5e62f))

* Update README.md ([`8fc9ae1`](https://github.com/blockchain-certificates/cert-issuer/commit/8fc9ae1f7b142e7883ea3763e3be4bba0b110fcc))

* Merge pull request #173 from blockchain-certificates/wip_etherscan_nonce

#172 - Etherscan nonce uses pending instead of latest. ([`76141de`](https://github.com/blockchain-certificates/cert-issuer/commit/76141de1b21ab8bc50c181d75ed1ea421d834feb))

* #172 - Changing over to pending for get_balance as well. ([`a745bab`](https://github.com/blockchain-certificates/cert-issuer/commit/a745bab4f148e3276e1aa54f8f7f7696eca61cff))

* #172 - Changing over to pending for get_balance as well. ([`b0cb424`](https://github.com/blockchain-certificates/cert-issuer/commit/b0cb4241f6094a30dc9b9bcd7dc9576815a8084b))

* Bump v3-alpha schema to 3.0.0a4 ([`24a4f4f`](https://github.com/blockchain-certificates/cert-issuer/commit/24a4f4f8ff202e51b77cc585b128ce9d862d49e2))

* Bump v3-alpha schema to 3.0.0a3 ([`c64f477`](https://github.com/blockchain-certificates/cert-issuer/commit/c64f477e1000307a9d7db43c632d3d7c749f4383))

* Fix test using proof instead of signature for v3 ([`df2a44f`](https://github.com/blockchain-certificates/cert-issuer/commit/df2a44f8b36c8885a0da2df3080e05a006b7496e))

* v3-alpha schema updates ([`625b1f1`](https://github.com/blockchain-certificates/cert-issuer/commit/625b1f169fa52e3accd35eb3e56be644c72db190))

* RI etherscan changes from v2 to v3 ([`830ee9d`](https://github.com/blockchain-certificates/cert-issuer/commit/830ee9d8ff2860976138dca8f2440c571e5d2170))

* Merge pull request #168 from blockchain-certificates/etherscan-api

Etherscan api key was never being used - fixed. ([`eccb187`](https://github.com/blockchain-certificates/cert-issuer/commit/eccb187a734ef2d9fd3d8300223bd703c1b4a2c5))

* Etherscan api key was never being used - fixed. ([`983c3d3`](https://github.com/blockchain-certificates/cert-issuer/commit/983c3d35f87487fe84288d5759b1044ba34acfa4))

* Merge pull request #167 from blockchain-certificates/etherscan-api-key

Raise a broadcast error if etherscan api error #166 ([`951f282`](https://github.com/blockchain-certificates/cert-issuer/commit/951f28284659d7d8a20560416e0b0cc5a7df4bb3))

* Merge pull request #115 from AnthonyRonning/master

Removing 2nd instance of logger ([`c984a62`](https://github.com/blockchain-certificates/cert-issuer/commit/c984a622ae1b3c1b8ac15958ce5e99f49e0931d8))

* Removing 2nd instance of logger

Logging is happening twice, due to `configure_logger()` at the beginning of the method and this one at the end. ([`67a6a06`](https://github.com/blockchain-certificates/cert-issuer/commit/67a6a0651421c3965dfddf0d68c1c5ca1963d57e))

* Merge pull request #113 from AnthonyRonning/master

#112 - Specifying Coincurve version to fix ethereum installation error ([`26f842a`](https://github.com/blockchain-certificates/cert-issuer/commit/26f842ab4bee1577f629e196abf5c2ff85714960))

* #112 - Specifying Coincurve version to fix ethereum installation error ([`f79e48d`](https://github.com/blockchain-certificates/cert-issuer/commit/f79e48dacf6fddc8b3da2630670ee4aca8862937))

* Merge pull request #109 from AnthonyRonning/master

Force ethereum python version to 2.3.1 (#107) ([`1a3c353`](https://github.com/blockchain-certificates/cert-issuer/commit/1a3c353fb8fcc462d5eaedba655c35f6a13fd3d4))

* Force ethereum python version to 2.3.1 (#107) ([`bff217f`](https://github.com/blockchain-certificates/cert-issuer/commit/bff217f3dced5d3eb7d4fd2027a80d16b3da50f1))

* Merge pull request #98 from AnthonyRonning/master

Fixing UnboundLocalError: local variable ‘cost_constants’ error ([`815e2ae`](https://github.com/blockchain-certificates/cert-issuer/commit/815e2aed87c28ce209136533621225a754be32ea))

* Rev version to 2.0.15 ([`7b8f327`](https://github.com/blockchain-certificates/cert-issuer/commit/7b8f32787d67b5565e299a020b0f096a6c95f944))

* Fixing UnboundLocalError: local variable ‘cost_constants’  error ([`51caa56`](https://github.com/blockchain-certificates/cert-issuer/commit/51caa56017b48b0b3f97ad63291a7d6eec6a038c))

* remove mock workaround; not needed ([`7c7b96a`](https://github.com/blockchain-certificates/cert-issuer/commit/7c7b96a4313669586c71fca8ab8531626ee7dab8))

* update cert-core and fix mocknet ([`99dfd57`](https://github.com/blockchain-certificates/cert-issuer/commit/99dfd57762adf756ecce997b6a59a6e0390ca25a))

* Merge pull request #97 from lparkerlm/master

Adding a document for PyCharm users. ([`763ce1b`](https://github.com/blockchain-certificates/cert-issuer/commit/763ce1b14695c11980aac1aefcf60cb0607ad852))

* Trying to fix image links. ([`31bbacc`](https://github.com/blockchain-certificates/cert-issuer/commit/31bbaccf85353c717ce86ab288095115d7c9a050))

* Adding a document to help folks get cert-issuer going in the PyCharm IDE. ([`322ec65`](https://github.com/blockchain-certificates/cert-issuer/commit/322ec6501a74db6c88b674192e0c638ea4acd0fa))

* Merge pull request #96 from AnthonyRonning/master

Gentle touch to the README to mention the Ethereum blockchain explorer. ([`64e22ff`](https://github.com/blockchain-certificates/cert-issuer/commit/64e22ff33e1ba5778e6207eba3456148ab09ce3d))

* Gentle touch to the README to mention the Ethereum blockchain explorer. ([`ea783cf`](https://github.com/blockchain-certificates/cert-issuer/commit/ea783cfd1241a8049150dcbdbed8e5d0c39a8672))

* Merge pull request #95 from AnthonyRonning/master

#92 - Fix for namespace and dependency conflicts with bitcoin and ethereum libraries (fixed). ([`6f63f9e`](https://github.com/blockchain-certificates/cert-issuer/commit/6f63f9e371d14d99772265234ca451fc1d4496e4))

* Removing the version number from the blockchain_handlers submodule. ([`65f7686`](https://github.com/blockchain-certificates/cert-issuer/commit/65f768602f02e6ed0a673016023891bd8444500c))

* Merge pull request #90 from AnthonyRonning/master

Removed ethereum testnet, should use ropsten instead ([`b560b6b`](https://github.com/blockchain-certificates/cert-issuer/commit/b560b6b4cdf5b500d29dc7f45230e0bd52c5f791))
---
sponsor: "Canto"
slug: "2023-10-canto"
date: "2023-11-20"
title: "Canto Liquidity Mining Protocol"
findings: "https://github.com/code-423n4/2023-10-canto-findings/issues"
contest: 288
---

# Overview

## About C4

Code4rena (C4) is an open organization consisting of security researchers, auditors, developers, and individuals with domain expertise in smart contracts.

A C4 audit is an event in which community participants, referred to as Wardens, review, audit, or analyze smart contract logic in exchange for a bounty provided by sponsoring projects.

During the audit outlined in this document, C4 conducted an analysis of the Canto Liquidity Mining Protocol smart contract system written in Solidity. The audit took place between October 3 — October 6 2023.

## Wardens

63 Wardens contributed reports to the Canto Liquidity Mining Protocol:

  1. [maanas](https://code4rena.com/@maanas)
  2. [ni8mare](https://code4rena.com/@ni8mare)
  3. [Satyam\_Sharma](https://code4rena.com/@Satyam_Sharma)
  4. [Banditx0x](https://code4rena.com/@Banditx0x)
  5. [adriro](https://code4rena.com/@adriro)
  6. [HChang26](https://code4rena.com/@HChang26)
  7. [kutugu](https://code4rena.com/@kutugu)
  8. [sces60107](https://code4rena.com/@sces60107)
  9. [0xweb3boy](https://code4rena.com/@0xweb3boy)
  10. [0xDING99YA](https://code4rena.com/@0xDING99YA)
  11. [3docSec](https://code4rena.com/@3docSec)
  12. [0xWaitress](https://code4rena.com/@0xWaitress)
  13. [emerald7017](https://code4rena.com/@emerald7017)
  14. [twicek](https://code4rena.com/@twicek)
  15. [0xpiken](https://code4rena.com/@0xpiken)
  16. [hunter\_w3b](https://code4rena.com/@hunter_w3b)
  17. [niser93](https://code4rena.com/@niser93)
  18. [radev\_sw](https://code4rena.com/@radev_sw)
  19. [albahaca](https://code4rena.com/@albahaca)
  20. [0xAnah](https://code4rena.com/@0xAnah)
  21. [JCK](https://code4rena.com/@JCK)
  22. [hihen](https://code4rena.com/@hihen)
  23. [MatricksDeCoder](https://code4rena.com/@MatricksDeCoder)
  24. [JP\_Courses](https://code4rena.com/@JP_Courses)
  25. [0xdice91](https://code4rena.com/@0xdice91)
  26. [cookedcookee](https://code4rena.com/@cookedcookee)
  27. [sandy](https://code4rena.com/@sandy)
  28. [ZanyBonzy](https://code4rena.com/@ZanyBonzy)
  29. [invitedtea](https://code4rena.com/@invitedtea)
  30. [naman1778](https://code4rena.com/@naman1778)
  31. [SAQ](https://code4rena.com/@SAQ)
  32. [SY\_S](https://code4rena.com/@SY_S)
  33. [tabriz](https://code4rena.com/@tabriz)
  34. [shamsulhaq123](https://code4rena.com/@shamsulhaq123)
  35. [pipidu83](https://code4rena.com/@pipidu83)
  36. [Raihan](https://code4rena.com/@Raihan)
  37. [lsaudit](https://code4rena.com/@lsaudit)
  38. [Polaris\_tow](https://code4rena.com/@Polaris_tow)
  39. [debo](https://code4rena.com/@debo)
  40. [Mike\_Bello90](https://code4rena.com/@Mike_Bello90)
  41. [0xTheC0der](https://code4rena.com/@0xTheC0der)
  42. [Eurovickk](https://code4rena.com/@Eurovickk)
  43. [marqymarq10](https://code4rena.com/@marqymarq10)
  44. [orion](https://code4rena.com/@orion)
  45. [wahedtalash77](https://code4rena.com/@wahedtalash77)
  46. [xAriextz](https://code4rena.com/@xAriextz)
  47. [BoRonGod](https://code4rena.com/@BoRonGod)
  48. [gzeon](https://code4rena.com/@gzeon)
  49. [SovaSlava](https://code4rena.com/@SovaSlava)
  50. [matrix\_0wl](https://code4rena.com/@matrix_0wl)
  51. [taner2344](https://code4rena.com/@taner2344)
  52. [Topmark](https://code4rena.com/@Topmark)
  53. [0x3b](https://code4rena.com/@0x3b)
  54. [100su](https://code4rena.com/@100su)
  55. [zpan](https://code4rena.com/@zpan)
  56. GKBG ([KKat7531](https://code4rena.com/@KKat7531) and [Stoicov](https://code4rena.com/@Stoicov))
  57. [BRONZEDISC](https://code4rena.com/@BRONZEDISC)
  58. [lukejohn](https://code4rena.com/@lukejohn)
  59. [IceBear](https://code4rena.com/@IceBear)
  60. [0xAadi](https://code4rena.com/@0xAadi)
  61. [pep7siup](https://code4rena.com/@pep7siup)
  62. [tpiliposian](https://code4rena.com/@tpiliposian)

This audit was judged by [LSDan](https://code4rena.com/@LSDan).

Final report assembled by [thebrittfactor](https://twitter.com/brittfactorC4).

# Summary

The C4 analysis yielded an aggregated total of 6 unique vulnerabilities. Of these vulnerabilities, 1 received a risk rating in the category of HIGH severity and 5 received a risk rating in the category of MEDIUM severity.

Additionally, C4 analysis included 37 reports detailing issues with a risk rating of LOW severity or non-critical. There were also 16 reports recommending gas optimizations.

All of the issues presented here are linked back to their original finding.

# Scope

The code under review can be found within the [C4 Canto Liquidity Mining Protocol repository](https://github.com/code-423n4/2023-10-canto), and is composed of 2 smart contracts written in the Solidity programming language and includes 145 lines of Solidity code.

In addition to the known issues identified by the project team, a Code4rena bot race was conducted at the start of the audit. The winning bot, **IllIllI-bot** from warden IllIllI, generated the [Automated Findings report](https://gist.github.com/code423n4/59002a10bbf69fc556e1c1dd8765c458) and all findings therein were classified as out of scope.

# Severity Criteria

C4 assesses the severity of disclosed vulnerabilities based on three primary risk categories: high, medium, and low/non-critical.

High-level considerations for vulnerabilities span the following key areas when conducting assessments:

- Malicious Input Handling
- Escalation of privileges
- Arithmetic
- Gas use

For more information regarding the severity criteria referenced throughout the submission review process, please refer to the documentation provided on [the C4 website](https://code4rena.com), specifically our section on [Severity Categorization](https://docs.code4rena.com/awarding/judging-criteria/severity-categorization).

# High Risk Findings (1)
## [[H-01] Array Length of `tickTracking_ ` can be purposely increased to Brick Minting and Burning of most users' liquidity positions](https://github.com/code-423n4/2023-10-canto-findings/issues/114)
*Submitted by [Banditx0x](https://github.com/code-423n4/2023-10-canto-findings/issues/114), also found by [Banditx0x](https://github.com/code-423n4/2023-10-canto-findings/issues/82), [maanas](https://github.com/code-423n4/2023-10-canto-findings/issues/276), [emerald7017](https://github.com/code-423n4/2023-10-canto-findings/issues/253), [adriro](https://github.com/code-423n4/2023-10-canto-findings/issues/235), [twicek](https://github.com/code-423n4/2023-10-canto-findings/issues/221), [0xDING99YA](https://github.com/code-423n4/2023-10-canto-findings/issues/215), [0xpiken](https://github.com/code-423n4/2023-10-canto-findings/issues/201), [3docSec](https://github.com/code-423n4/2023-10-canto-findings/issues/68), and [0xWaitress](https://github.com/code-423n4/2023-10-canto-findings/issues/11)*

### Lines of code

<https://github.com/code-423n4/2023-10-canto/blob/40edbe0c9558b478c84336aaad9b9626e5d99f34/canto_ambient/contracts/mixins/LiquidityMining.sol#L24-L35><br>
<https://github.com/code-423n4/2023-10-canto/blob/40edbe0c9558b478c84336aaad9b9626e5d99f34/canto_ambient/contracts/mixins/LiquidityMining.sol#L122>

### Impact

A malicious user can brick minting, burning and harvesting of liquidity for almost all liquidity providers.

*Important NOTE*: This is a different vector from another gas issue, which is iterating over too many ticks in `(int24 i = lowerTick + 10; i <= upperTick - 10; ++i)`. That issue affects wide liquidity positions, while this attack vector affects even liquidity positions with a relatively small number of ticks.

### Proof of Concept

When `accrueConcentratedPositionTimeWeightedLiquidity` is called, under most conditions for every potentially eligible tick, it will iterate over every `tickTrackingData` in `tickTracking`:

```solidity
while (time < block.timestamp && tickTrackingIndex < numTickTracking)
```

`tickTracking` is iterated by `tickTrackingIndex++;`

The array mapped by `tickTracking_` is increased by 1 for a tick every time a trade through the liquidity pool changes the price from a different tick to this tick. This is implemented in the `crossTicks` function:

```solidity
    function crossTicks(
        bytes32 poolIdx,
        int24 exitTick,
        int24 entryTick
    ) internal {
        uint256 numElementsExit = tickTracking_[poolIdx][exitTick].length;
        tickTracking_[poolIdx][exitTick][numElementsExit - 1]
            .exitTimestamp = uint32(block.timestamp);
        StorageLayout.TickTracking memory tickTrackingData = StorageLayout
            .TickTracking(uint32(block.timestamp), 0);
        tickTracking_[poolIdx][entryTick].push(tickTrackingData);
    }
```

A user could purposely increase the length of the `tickTracking_` array and cause the gas limit to be reached whenever the array is looped over.

The price impact required to cross a tick is from 0 to 1 bps, with 1 bps as the tick width. This is already extremely small, but the attacker could have the swap amount be a very small fraction of a bps if they first swap to make the price end very close to a tick boundary, then execute multiple extremely small swaps which bounce the price back and forth over the tick boundary.

Note that the CANTO liquidity rewards are targeted to stable pools. An attacker can be quite confident, for example, that a USDC/USDT pool will trade at around `$`1, and the ticks closest to `$`1 will always be eligible for rewards and therefore be looped over by all rewardable positions when `accrueConcentratedPositionTimeWeightedLiquidity` is called. Therefore, the attack can be targeted to just one or two ticks to affect almost every user.

`accrueConcentratedPositionTimeWeightedLiquidity` is called during minting, burning and harvesting liquidity positions. Therefore, this gas griefing attack will make all these functions revert for almost every user. This would basically break the functionality of concentrated liquidity pools on Ambient.

Contrast the effect to the cost to the attacker: using the aforementioned attack vector the main cost to the attacker will be the gas costs of performing the swaps. This is far lower than the damage that is done to the protocol/users.

One additional factor which makes this attack easy to execute, is that crossing ticks, even if the entry and exit is within the same `block.timestamp`, adds to the array length. Tracking this is unnecessary, because the tick was active for 0 blocks, and therefore, the time delta and allocated rewards is zero.

### Recommended Mitigation Steps

One immediate step would to `pop()` `tickTrackingData` as soon as the `exitTimestamp == entryTimestamp`. This happens to the last element of the array when `crossTicks` is called. Tracking this is unnecessary, because the tick was active for 0 blocks, and therefore, the time delta and allocated rewards is zero.

The documentation stated that CANTO rewards are meant to be distributed for stable pools for this codebase. The term "stable" could have different interpretations, but this recommendation assumes that this refers to stablecoin-like or pegged asset pairs such as stETH/WETH, USDT/USDC etc.

Instead of iterating through every tick, one could assume a range where the stable assets could lie and then reward all positions that lie within the specified range; in this case, +/- 10 ticks of the price tick.

This makes an assumption that these "stable assets" will actually stay pegged to each other. However, the current accounting architecture has multiple problems:

- Given the high number of loops required by the current accounting mechanism, there are multiple reasons that gas could run out. This includes iterating through too many ticks or having too many tick entries/exits.

- The current mechanism increases the gas costs of all minting, burning and harvesting.

- DOS attacks like the one described in this issue are possible.

Assuming a stable price has the downside of misallocating rewards if the stable assets depeg from each other. However, this may be a reasonable tradeoff to prevent this DOS attack.

### Assessed type

DoS

**[OpenCoreCH (Canto) confirmed](https://github.com/code-423n4/2023-10-canto-findings/issues/114#issuecomment-1757196983)**

*Note: for full discussion, see [here](https://github.com/code-423n4/2023-10-canto-findings/issues/114)*.

***
 
# Medium Risk Findings (5)
## [[M-01] The Liquidity mining callpath sidecar owner can pull native tokens from the `Dex`](https://github.com/code-423n4/2023-10-canto-findings/issues/295)
*Submitted by [maanas](https://github.com/code-423n4/2023-10-canto-findings/issues/295)*

The owner of the liquidity mining sidecar can pull the native coins that are stored in the `CrocSwapDex` to reward the users.

### Proof of Concept

The `setConcRewards` and `setAmbRewards` functions don't check if the quoted amount of rewards are actually sent by the caller. This allows the owner to specify any total amount of native coin which are available in the `CrocSwapDex` from which the funds will be used when distributing the rewards.

```solidity
    function setConcRewards(bytes32 poolIdx, uint32 weekFrom, uint32 weekTo, uint64 weeklyReward) public payable {
        // require(msg.sender == governance_, "Only callable by governance");
        require(weekFrom % WEEK == 0 && weekTo % WEEK == 0, "Invalid weeks");
        while (weekFrom <= weekTo) {
            concRewardPerWeek_[poolIdx][weekFrom] = weeklyReward;
            weekFrom += uint32(WEEK);
        }
    }
```
<https://github.com/code-423n4/2023-10-canto/blob/40edbe0c9558b478c84336aaad9b9626e5d99f34/canto_ambient/contracts/callpaths/LiquidityMiningPath.sol#L65C7-L72>

```solidity
    function setAmbRewards(bytes32 poolIdx, uint32 weekFrom, uint32 weekTo, uint64 weeklyReward) public payable {
        // require(msg.sender == governance_, "Only callable by governance");
        require(weekFrom % WEEK == 0 && weekTo % WEEK == 0, "Invalid weeks");
        while (weekFrom <= weekTo) {
            ambRewardPerWeek_[poolIdx][weekFrom] = weeklyReward;
            weekFrom += uint32(WEEK);
        }
    }
```
<https://github.com/code-423n4/2023-10-canto/blob/40edbe0c9558b478c84336aaad9b9626e5d99f34/canto_ambient/contracts/callpaths/LiquidityMiningPath.sol#L74-L81>

According to [Ambient Docs](https://docs.ambient.finance/developers/token-transfers#native-ethereum) they allow for deposits in native tokens.

### Demo

Update TestLiquidityMining.js:

The funds added using `hardhat.setBalance()` is being used by the owner to distribute rewards

```diff
diff --git a/canto_ambient/test_canto/TestLiquidityMining.js b/canto_ambient/test_canto/TestLiquidityMining.js
index bd21a32..b917308 100644
--- a/canto_ambient/test_canto/TestLiquidityMining.js
+++ b/canto_ambient/test_canto/TestLiquidityMining.js
@@ -7,6 +7,7 @@ const { time } = require("@nomicfoundation/hardhat-network-helpers");
 var keccak256 = require("@ethersproject/keccak256").keccak256;
 
 const chai = require("chai");
+const { network, ethers } = require("hardhat");
 const abi = new AbiCoder();
 
 const BOOT_PROXY_IDX = 0;
@@ -218,7 +219,6 @@ describe("Liquidity Mining Tests", function () {
 		);
 		tx = await dex.userCmd(2, mintConcentratedLiqCmd, {
 			gasLimit: 6000000,
-			value: ethers.utils.parseUnits("10", "ether"),
 		});
 		await tx.wait();
 
@@ -243,6 +243,17 @@ describe("Liquidity Mining Tests", function () {
 			BigNumber.from("999898351768")
 		);
 
+		let dexBal = await ethers.provider.getBalance(dex.address);
+		expect(dexBal.eq(0)).to.be.eq(true);
+
+		// dex gains native token from other methods
+		await network.provider.send("hardhat_setBalance", [
+			dex.address,
+			ethers.utils.parseEther("2").toHexString(),
+		  ]);
+		dexBal = await ethers.provider.getBalance(dex.address);
+		expect(dexBal.eq(ethers.utils.parseEther("2"))).to.be.eq(true);
+
 		//////////////////////////////////////////////////
 		// SET LIQUIDITY MINING REWARDS FOR CONCENTRATED LIQUIDITY
 		//////////////////////////////////////////////////
```

### Tools Used

Hardhat

### Recommended Mitigation Steps

Add a `msg.value` check in the rewards function to see that the total value is passed when call the functions.

```diff
diff --git a/canto_ambient/contracts/callpaths/LiquidityMiningPath.sol b/canto_ambient/contracts/callpaths/LiquidityMiningPath.sol
index e6c63f7..44dd338 100644
--- a/canto_ambient/contracts/callpaths/LiquidityMiningPath.sol
+++ b/canto_ambient/contracts/callpaths/LiquidityMiningPath.sol
@@ -65,6 +65,7 @@ contract LiquidityMiningPath is LiquidityMining {
     function setConcRewards(bytes32 poolIdx, uint32 weekFrom, uint32 weekTo, uint64 weeklyReward) public payable {
         // require(msg.sender == governance_, "Only callable by governance");
         require(weekFrom % WEEK == 0 && weekTo % WEEK == 0, "Invalid weeks");
+        require((1 +(weekTo - weekFrom) / WEEK) * weeklyReward == msg.value);
         while (weekFrom <= weekTo) {
             concRewardPerWeek_[poolIdx][weekFrom] = weeklyReward;
             weekFrom += uint32(WEEK);
```

### Assessed type

Rug-Pull

**[OpenCoreCH (Canto) acknowledged and commented](https://github.com/code-423n4/2023-10-canto-findings/issues/295#issuecomment-1792892349):**
> Rewards will be set and sent in the same Canto governance proposal.

***

## [[M-02] If `dt` is not updated accurately, `timeWeightedWeeklyPositionInRangeConcLiquidity_` might be updated incorrectly](https://github.com/code-423n4/2023-10-canto-findings/issues/290)
*Submitted by [ni8mare](https://github.com/code-423n4/2023-10-canto-findings/issues/290)*

In the function `accrueConcentratedPositionTimeWeightedLiquidity`, inside the while block, `dt` is initialised as:

        uint32 dt = uint32(
           nextWeek < block.timestamp
           ? nextWeek - time
           : block.timestamp - time
       );

<https://github.com/code-423n4/2023-10-canto/blob/40edbe0c9558b478c84336aaad9b9626e5d99f34/canto_ambient/contracts/mixins/LiquidityMining.sol#L98-L102>

If `tickTracking.exitTimestamp != 0` then the following else block is executed on line 117:

    else {
       // Tick is no longer active
       if (tickTracking.exitTimestamp < nextWeek) {
          // Exit was in this week, continue with next tick
          tickActiveEnd = tickTracking.exitTimestamp;
          tickTrackingIndex++;
          dt = tickActiveEnd - tickActiveStart;
       } else {
         // Exit was in next week, we need to consider the current tick there (i.e. not increase the index)
         tickActiveEnd = nextWeek;
        }
     }

<https://github.com/code-423n4/2023-10-canto/blob/40edbe0c9558b478c84336aaad9b9626e5d99f34/canto_ambient/contracts/mixins/LiquidityMining.sol#L117-L128>

`dt` is now updated to `tickActiveEnd - tickActiveStart;` when `tickTracking.exitTimestamp < nextWeek` as seen in the if block of the outer else block above.

But, when `tickTracking.exitTimestamp > nextWeek`, in the inner else block the value of `dt` is not updated:

     else {
         // Exit was in next week, we need to consider the current tick there (i.e. not increase the index)
         tickActiveEnd = nextWeek;
         //@audit - No update on dt value
        }

Inside this else block as well, `dt` must equal `tickActiveEnd - tickActiveStart;`, where `tickActiveEnd = nextWeek;`. Without this update, if `tickTracking.exitTimestamp > nextWeek`, then `dt = nextWeek - time` or `dt = block.timestamp - time` as it was declared initially. For example, let's say that it was the former, that is, `dt = nextWeek - time` (according to the initial declaration). Assume that `tickActiveStart = tickTracking.enterTimestamp` (this is possible when [tickTracking.enterTimestamp > time](https://github.com/code-423n4/2023-10-canto/blob/40edbe0c9558b478c84336aaad9b9626e5d99f34/canto_ambient/contracts/mixins/LiquidityMining.sol#L110-L113)). Had the else block above (check @audit tag), updated `dt`, then `dt = tickActiveEnd - tickActiveStart;` => `dt = nextWeek - tickTracking.enterTimestamp`

So, on comparing again, initially -> `dt = nextWeek - time` and had there been an update on `dt` at the audit tag, `dt` would now be -> `dt = nextWeek - tickTracking.enterTimestamp`. Note that here, `tickTracking.enterTimestamp > time` (check the above para). So, `nextWeek - tickTracking.enterTimestamp < nextWeek - time`. That means `dt` would be a smaller value had it been equal to `nextWeek - tickTracking.enterTimestamp`. But, since it's not updated, `dt` equals `nextWeek - time`, which is a bigger value.

`dt` is used to increase the value of time (used as an iterator in while loop). Since `dt` is a bigger value than required, the number of iterations of the while loop would be less than what it should be. This means that fewer iterations would be used to update `timeWeightedWeeklyPositionInRangeConcLiquidity_` on line [129](https://github.com/code-423n4/2023-10-canto/blob/40edbe0c9558b478c84336aaad9b9626e5d99f34/canto_ambient/contracts/mixins/LiquidityMining.sol#L129)

    timeWeightedWeeklyPositionInRangeConcLiquidity_[poolIdx][posKey][currWeek][i] +=
                                (tickActiveEnd - tickActiveStart) * liquidity;

`timeWeightedWeeklyPositionInRangeConcLiquidity_` is used to calculate the `rewardsToSend` value in `claimConcentratedRewards` function. If `timeWeightedWeeklyPositionInRangeConcLiquidity_` is incorrect, then the rewards to be sent to the user will be calculated incorrectly.

<https://github.com/code-423n4/2023-10-canto/blob/40edbe0c9558b478c84336aaad9b9626e5d99f34/canto_ambient/contracts/mixins/LiquidityMining.sol#L181-L188>

    uint256 overallInRangeLiquidity = timeWeightedWeeklyGlobalConcLiquidity_[poolIdx][week];
       if (overallInRangeLiquidity > 0) {
          uint256 inRangeLiquidityOfPosition;
          for (int24 j = lowerTick + 10; j <= upperTick - 10; ++j) {
             inRangeLiquidityOfPosition += timeWeightedWeeklyPositionInRangeConcLiquidity_[poolIdx][posKey][week][j];
           }
           // Percentage of this weeks overall in range liquidity that was provided by the user times the overall weekly rewards
           rewardsToSend += inRangeLiquidityOfPosition * concRewardPerWeek_[poolIdx][week] / overallInRangeLiquidity; //@audit - rewards to send will be less

Also, due to fewer number of iterations, `tickTrackingIndexAccruedUpTo_` might not be updated correctly.

    if (tickTrackingIndex != origIndex) {
      tickTrackingIndexAccruedUpTo_[poolIdx][posKey][i] = tickTrackingIndex;
    }

### Proof of Concept

        /// @notice Accrues the in-range time-weighted concentrated liquidity for a position by going over the tick entry / exit history
        /// @dev Needs to be called whenever a position is modified
        function accrueConcentratedPositionTimeWeightedLiquidity(
            address payable owner,
            bytes32 poolIdx,
            int24 lowerTick,
            int24 upperTick
        ) internal {
            RangePosition72 storage pos = lookupPosition(
                owner,
                poolIdx,
                lowerTick,
                upperTick
            );
            bytes32 posKey = encodePosKey(owner, poolIdx, lowerTick, upperTick);
            uint32 lastAccrued = timeWeightedWeeklyPositionConcLiquidityLastSet_[
                poolIdx
            ][posKey];
            // Only set time on first call
            if (lastAccrued != 0) {
                uint256 liquidity = pos.liquidity_;
                for (int24 i = lowerTick + 10; i <= upperTick - 10; ++i) {
                    uint32 tickTrackingIndex = tickTrackingIndexAccruedUpTo_[poolIdx][posKey][i];
                    uint32 origIndex = tickTrackingIndex;
                    uint32 numTickTracking = uint32(tickTracking_[poolIdx][i].length);
                    uint32 time = lastAccrued;
                    // Loop through all in-range time spans for the tick or up to the current time (if it is still in range)
                    while (time < block.timestamp && tickTrackingIndex < numTickTracking) {
                        TickTracking memory tickTracking = tickTracking_[poolIdx][i][tickTrackingIndex];
                        uint32 currWeek = uint32((time / WEEK) * WEEK);
                        uint32 nextWeek = uint32(((time + WEEK) / WEEK) * WEEK);
                        uint32 dt = uint32(
                            nextWeek < block.timestamp
                                ? nextWeek - time
                                : block.timestamp - time
                        );
                        uint32 tickActiveStart; // Timestamp to use for the liquidity addition
                        uint32 tickActiveEnd;
                        if (tickTracking.enterTimestamp < nextWeek) {
                            // Tick was active before next week, need to add the liquidity
                            if (tickTracking.enterTimestamp < time) {
                                // Tick was already active when last claim happened, only accrue from last claim timestamp
                                tickActiveStart = time;
                            } else {
                                // Tick has become active this week
                                tickActiveStart = tickTracking.enterTimestamp;
                            }
                            if (tickTracking.exitTimestamp == 0) {
                                // Tick still active, do not increase index because we need to continue from here
                                tickActiveEnd = uint32(nextWeek < block.timestamp ? nextWeek : block.timestamp);
                            } else {
                                // Tick is no longer active
                                if (tickTracking.exitTimestamp < nextWeek) {
                                    // Exit was in this week, continue with next tick
                                    tickActiveEnd = tickTracking.exitTimestamp;
                                    tickTrackingIndex++;
                                    dt = tickActiveEnd - tickActiveStart;
                                } else {
                                    // Exit was in next week, we need to consider the current tick there (i.e. not increase the index)
                                    tickActiveEnd = nextWeek;
                                }
                            }
                            timeWeightedWeeklyPositionInRangeConcLiquidity_[poolIdx][posKey][currWeek][i] +=
                                (tickActiveEnd - tickActiveStart) * liquidity;
                        }
                        time += dt;
                    }
                    if (tickTrackingIndex != origIndex) {
                        tickTrackingIndexAccruedUpTo_[poolIdx][posKey][i] = tickTrackingIndex;
                    }
                }
            } else {
                for (int24 i = lowerTick + 10; i <= upperTick - 10; ++i) {
                    uint32 numTickTracking = uint32(tickTracking_[poolIdx][i].length);
                    if (numTickTracking > 0) {
                        if (tickTracking_[poolIdx][i][numTickTracking - 1].exitTimestamp == 0) {
                            // Tick currently active
                            tickTrackingIndexAccruedUpTo_[poolIdx][posKey][i] = numTickTracking - 1;
                        } else {
                            tickTrackingIndexAccruedUpTo_[poolIdx][posKey][i] = numTickTracking;
                        }
                    }
                }
            }
            timeWeightedWeeklyPositionConcLiquidityLastSet_[poolIdx][
                posKey
            ] = uint32(block.timestamp);
        }

### Recommended Mitigation Steps

Add the line `dt = tickActiveEnd - tickActiveStart` in the place of the @audit tag, as shown above.

**[OpenCoreCH (Canto) confirmed and commented](https://github.com/code-423n4/2023-10-canto-findings/issues/290#issuecomment-1757581037):**
 > Note that if the mentioned `else` branch is reached, `dt` is necessarily set to `nextWeek - time`, it cannot be `block.timestamp - time` (if the tick was exited in the next week, the next week cannot be in the future and greater than the block timestamp). So the only possible difference is regarding `tickActiveStart`, namely when `tickActiveStart = tickTracking.enterTimestamp` (in the other case, when `tickActiveStart = time`, we have `dt = nextWeek - time = tickActiveEnd - tickActiveStart`).
> 
> I agree with the warden that in this particular case, the logic for updating `dt` is different in the `if` and `else` branch, which should not be the case. However, I think the logic in the `if` branch is wrong, not in the `else`: We want to set `dt` such that the next `time` value is equal to `tickActiveEnd` (because we accrued up to `tickActiveEnd`). To achieve this in all cases, we need to set `dt = tickActiveEnd - time` in the `if` block. Otherwise, when `tickTracking.enterTimestamp > time` we only add the time where the tick was in range to `time` (but not the time before that where the tick was out of range). Because we are also increasing the tick tracking index, this should not cause any problems in practice (the next enter timestamp will be greater than `time` by definition and we will only start accruing from there on again), but I think it should still be changed.

*Note: for full discussion, see [here](https://github.com/code-423n4/2023-10-canto-findings/issues/290)*.

***

## [[M-03] Rewards cannot be transferred when calling protocol command](https://github.com/code-423n4/2023-10-canto-findings/issues/239)
*Submitted by [adriro](https://github.com/code-423n4/2023-10-canto-findings/issues/239), also found by [HChang26](https://github.com/code-423n4/2023-10-canto-findings/issues/116)*

Rewards are set up using protocol commands, but its entry point is not payable.

Rewards can be set up by protocol authorities using the functions `setConcRewards()` and `setAmbRewards()` present in the LiquidityMiningPath contracts. These two are part of the "command" pattern used in the protocol: the main entry point receives *commands* which are then routed to the proper place using *codes*.

The protocol command flow starts at the `CrocSwapDex` contract:

<https://github.com/code-423n4/2023-10-canto/blob/main/canto_ambient/contracts/CrocSwapDex.sol#L103-L106>

```solidity
103:     function protocolCmd (uint16 callpath, bytes calldata cmd, bool sudo)
104:         protocolOnly(sudo) public payable override {
105:         callProtocolCmd(callpath, cmd);
106:     }
```

<https://github.com/code-423n4/2023-10-canto/blob/main/canto_ambient/contracts/mixins/ProxyCaller.sol#L22-L28>

```solidity
22:     function callProtocolCmd (uint16 proxyIdx, bytes calldata input) internal
23:         returns (bytes memory) {
24:         assertProxy(proxyIdx);
25:         (bool success, bytes memory output) = proxyPaths_[proxyIdx].delegatecall(
26:             abi.encodeWithSignature("protocolCmd(bytes)", input));
27:         return verifyCallResult(success, output);
28:     }
```

The `protocolCmd()` function checks the call is properly authorized and calls `callProtocolCmd()`, which then executes a `delegatecall` to the corresponding implementation, in this case the `LiquidityMiningPath` contract:

<https://github.com/code-423n4/2023-10-canto/blob/main/canto_ambient/contracts/callpaths/LiquidityMiningPath.sol#L26-L37>

```solidity
26:     function protocolCmd(bytes calldata cmd) public virtual {
27:         (uint8 code, bytes32 poolHash, uint32 weekFrom, uint32 weekTo, uint64 weeklyReward) =
28:             abi.decode(cmd, (uint8, bytes32, uint32, uint32, uint64));
29: 
30:         if (code == ProtocolCmd.SET_CONC_REWARDS_CODE) {
31:             setConcRewards(poolHash, weekFrom, weekTo, weeklyReward);
32:         } else if (code == ProtocolCmd.SET_AMB_REWARDS_CODE) {
33:             setAmbRewards(poolHash, weekFrom, weekTo, weeklyReward);
34:         } else {
35:             revert("Invalid protocol command");
36:         }
37:     }
```

While `CrocSwapDex::protocolCmd()` is payable, its counterpart in `LiquidityMiningPath` is not. This means that rewards cannot be transferred while setting them up, rejecting any command that has positive `callvalue`.

### Recommendation

Make `LiquidityMiningPath::protocolCmd()` payable.

```diff
-   function protocolCmd(bytes calldata cmd) public virtual {
+   function protocolCmd(bytes calldata cmd) public virtual payable {
        (uint8 code, bytes32 poolHash, uint32 weekFrom, uint32 weekTo, uint64 weeklyReward) =
            abi.decode(cmd, (uint8, bytes32, uint32, uint32, uint64));

        if (code == ProtocolCmd.SET_CONC_REWARDS_CODE) {
            setConcRewards(poolHash, weekFrom, weekTo, weeklyReward);
        } else if (code == ProtocolCmd.SET_AMB_REWARDS_CODE) {
            setAmbRewards(poolHash, weekFrom, weekTo, weeklyReward);
        } else {
            revert("Invalid protocol command");
        }
    }
```

### Assessed type

Payable

**[141345 (lookout) commented](https://github.com/code-423n4/2023-10-canto-findings/issues/239#issuecomment-1752014651):**
 > `protocolCmd()` should be payable.
> 
> One walk around is to call `setAmbRewards()`/`setConcRewards()`directly to send funds. But seems the expected way is to use this contract through `delegatecall`, if the contract is deployed without this option, the described issue could be some problem.

**[OpenCoreCH (Canto) confirmed](https://github.com/code-423n4/2023-10-canto-findings/issues/239#issuecomment-1757450727)**

***

## [[M-04] Accrued liquidity can be lost and never be recovered for a given tick period. ](https://github.com/code-423n4/2023-10-canto-findings/issues/186)
*Submitted by [Satyam\_Sharma](https://github.com/code-423n4/2023-10-canto-findings/issues/186)*

Accrued liquidity can be lost and never be recovered for a given tick period due to not incrementing
`tickTrackingIndex`, which sets the tick end timestamp to `nextweek` and will start accruing liquidity for next tick period.

### Proof of Concept

`LiquidityMining.accrueConcentratedPositionTimeWeightedLiquidity` sets `tickActiveEnd = nextWeek` and doesn't increment `tickTrackingIndex`, which makes current tick period to end by setting `tickActiveEnd = nextWeek` and moves to next tick period without incrementing `tickTrackingIndex`. When tick is no longer active that is `tickTracking.exitTimestamp < nextWeek`, it means `tickTracking.exitTimestamp` should be strictly less than the `nextWeek` to set ` tickActiveEnd = tickTracking.exitTimestamp` and then calculate `dt` based on the `tickActiveStart` and `tickActiveEnd` values.


    else {
                                // Tick is no longer active
                                if (tickTracking.exitTimestamp < nextWeek) {
                                    // Exit was in this week, continue with next tick
                                    tickActiveEnd = tickTracking.exitTimestamp;//1697068700
                                    tickTrackingIndex++;
                                    dt = tickActiveEnd - tickActiveStart;
                                } else {
                                    // Exit was in next week, we need to consider the current tick there (i.e. not increase the index)
                                    tickActiveEnd = nextWeek;
                                }

Now the issue here, is with the `if` statement; `if (tickTracking.exitTimestamp < nextWeek)` calculates `dt` if
`exitTimestamp` is strictly lesser than the `nextWeek`. Suppose there is a condition in which user `exitTimestamp = nextWeek` i.e.; user exits the concentrated liquidity position with some `X` poolIdx with the `nextWeek` timestamp. Meaning when the `nextWeek` is about to end, the user triggers an exit and as soon as the exit triggers, this `if` statement will revert and `tickTrackingIndex` will not be incremented for that user or poolId. `tickTrackingIndexAccruedUpTo_[poolIdx][posKey][i]` and therefore, the accrued concentrated liquidity might be lost for a given tick period and will never be recovered due to setting `tickActiveEnd = nextWeek` in the `else` statement; which will declare the tick end and move to the next tick period to accrued liquidity .

### Recommended Mitigation Steps

Edit the `if` statement for `exitTimestamp`, which increments `tickTrackingIndex` when `tickTracking.exitTimestamp == nextWeek`:

```
 - if (tickTracking.exitTimestamp < nextWeek) {
            }
 +  if (tickTracking.exitTimestamp <= nextWeek) { 
            }
```

### Assessed type

Error

**[141345 (lookout) commented](https://github.com/code-423n4/2023-10-canto-findings/issues/186#issuecomment-1751976319):**
 > An edge case when `exitTimestamp == nextWeek`, rewards could be lost 
> 
> ```solidity
> File: canto_ambient/contracts/mixins/LiquidityMining.sol
> 24:     function crossTicks() internal {
> 
> 29:         uint256 numElementsExit = tickTracking_[poolIdx][exitTick].length;
> 30:         tickTracking_[poolIdx][exitTick][numElementsExit - 1]
> 31:             .exitTimestamp = uint32(block.timestamp);
> ```
> 
> Due to the low likelihood, high severity might not be appropriate.

**[OpenCoreCH (Canto) confirmed and commented](https://github.com/code-423n4/2023-10-canto-findings/issues/186#issuecomment-1757252292):**
 > Good point, requires quite a few conditions to actually cause damage (exactly aligned `exitTimestamp` and even then, the accrual has to happen a few weeks later with additional ticks that were in range since then for it to cause skipping ticks), but will definitely be fixed.

**[LSDan (judge) decreased severity to Medium](https://github.com/code-423n4/2023-10-canto-findings/issues/186#issuecomment-1769301330)**

*Note: for full discussion, see [here](https://github.com/code-423n4/2023-10-canto-findings/issues/186)*.

***

## [[M-05] Positions that are not eligible for rewards will affect the reward income of eligible positions](https://github.com/code-423n4/2023-10-canto-findings/issues/177)
*Submitted by [kutugu](https://github.com/code-423n4/2023-10-canto-findings/issues/177), also found by [sces60107](https://github.com/code-423n4/2023-10-canto-findings/issues/165) and Banditx0x ([1](https://github.com/code-423n4/2023-10-canto-findings/issues/98), [2](https://github.com/code-423n4/2023-10-canto-findings/issues/94))*

### Lines of code

<https://github.com/code-423n4/2023-10-canto/blob/40edbe0c9558b478c84336aaad9b9626e5d99f34/canto_ambient/contracts/mixins/LiquidityMining.sol#L181><br>
<https://github.com/code-423n4/2023-10-canto/blob/40edbe0c9558b478c84336aaad9b9626e5d99f34/canto_ambient/contracts/mixins/LiquidityMining.sol#L188><br>
<https://github.com/code-423n4/2023-10-canto/blob/40edbe0c9558b478c84336aaad9b9626e5d99f34/canto_ambient/contracts/mixins/LiquidityMining.sol#L48>

### Impact

When calculating reward distribution, the contract uses the current position's liquidity time weight divided by the total liquidity time weight of the pool, instead of the total liquidity time weight of the pool that meets the reward conditions.
This means that if there is a large amount of liquidity in the pool that is not eligible for rewards, the total weekly reward distribution will be much less than the `rewardPerWeek`, which should not be expected.

### Proof of Concept

```diff
diff --git a/canto_ambient/test_canto/TestLiquidityMining.js b/canto_ambient/test_canto/TestLiquidityMining.js
index bd21a32..617b070 100644
--- a/canto_ambient/test_canto/TestLiquidityMining.js
+++ b/canto_ambient/test_canto/TestLiquidityMining.js
@@ -32,7 +32,7 @@ chai.use(solidity);
 
 describe("Liquidity Mining Tests", function () {
 	it("deploy contracts and init pool", async function () {
-		const [owner] = await ethers.getSigners();
+		const [owner, others] = await ethers.getSigners();
 
 		////////////////////////////////////////////////
 		// DEPLOY AND MINT cNOTE and USDC
@@ -49,6 +49,14 @@ describe("Liquidity Mining Tests", function () {
 			owner.address,
 			ethers.utils.parseUnits("1000000", 6)
 		);
+		await cNOTE.deposit(
+			others.address,
+			ethers.utils.parseEther("1000000")
+		);
+		await USDC.deposit(
+			others.address,
+			ethers.utils.parseUnits("1000000", 6)
+		);
 
 		////////////////////////////////////////////////
 		// DEPLOY DEX CONTRACT AND ALL PROXIES
@@ -145,6 +153,17 @@ describe("Liquidity Mining Tests", function () {
 		);
 		await approveCNOTE.wait();
 
+		approveUSDC = await USDC.connect(others).approve(
+			dex.address,
+			BigNumber.from(10).pow(36)
+		);
+		await approveUSDC.wait();
+		approveCNOTE = await cNOTE.connect(others).approve(
+			dex.address,
+			BigNumber.from(10).pow(36)
+		);
+		await approveCNOTE.wait();
+
 		/* 
         /	2. set new pool liquidity (amount to lock up for new pool)
         /	   params = [code, liq]
@@ -222,6 +241,40 @@ describe("Liquidity Mining Tests", function () {
 		});
 		await tx.wait();
 
+		mintConcentratedLiqCmd = abi.encode(
+			[
+				"uint8",
+				"address",
+				"address",
+				"uint256",
+				"int24",
+				"int24",
+				"uint128",
+				"uint128",
+				"uint128",
+				"uint8",
+				"address",
+			],
+			[
+				11, // code (mint concentrated liquidity in base token liq)
+				cNOTE.address, // base token
+				USDC.address, // quote token
+				36000, // poolIDX
+				currentTick - 5, // tickLower
+				currentTick + 5, // tickUpper
+				BigNumber.from("100000000000000000000"), // amount of base token to send
+				BigNumber.from("16602069666338596454400000"), // min price
+				BigNumber.from("20291418481080506777600000"), // max price
+				0, // reserve flag
+				ZERO_ADDR, // lp conduit address (0 if not using)
+			]
+		);
+		tx = await dex.connect(others).userCmd(2, mintConcentratedLiqCmd, {
+			gasLimit: 6000000,
+			value: ethers.utils.parseUnits("10", "ether"),
+		});
+		await tx.wait();
+
 		////////////////////////////////////////////////
 		// SAMPLE SWAP TEST (swaps 2 USDC for cNOTE)
 		////////////////////////////////////////////////
@@ -300,9 +353,9 @@ describe("Liquidity Mining Tests", function () {
 		const dexBalAfter = await ethers.provider.getBalance(dex.address);
 		const ownerBalAfter = await ethers.provider.getBalance(owner.address);
 
-		// expect dex to have 2 less CANTO since we claimed for 2 weeks worth of rewards
+		// @audit Expect to have less CANTO rewards due to additional and not eligible for rewards liquidity
 		expect(dexBalBefore.sub(dexBalAfter)).to.equal(
-			BigNumber.from("2000000000000000000")
+			BigNumber.from("501412401683494542")
 		);
 	});
 });
```

In the pool, there is only one position that meets the reward conditions, and there is also one position that does not meet the conditions.

According to common sense, weekly rewards should be distributed to the only position that meets the reward conditions based on `rewardPerWeek`. However, in reality, you can see that the rewards that should be distributed every week have been reduced to `1/4` due to the ineligible position.

### Tools Used

Hardhat

### Recommended Mitigation Steps

Since the reward distribution of concentrated type rewards is conditionally restricted, the conditional restrictions should also be taken into account when calculating the total weight, rather than directly counting the total amount of liquidity.

### Assessed type

Context

**[OpenCoreCH (Canto) disputed and commented via duplicate Issue #94](https://github.com/code-423n4/2023-10-canto-findings/issues/94#issuecomment-1761327402):**
> Responding to this and [#98](https://github.com/code-423n4/2023-10-canto-findings/issues/98) here:
> 
> The warden seems to assume that `curve.concLiq_` is influenced by the width of a position, which is not the case. If someone creates a position with range [0, 1000] and liq. 100 or [480, 520] with liq. 100, `curve.concLiq_` will be 100 in both cases when the active tick is 500 (and not 0.1 & 2.5, which seems to be the assumption of the warden). This  can be seen in `TradeMatcher`, `LevelBook`, and `LiquidityMath`. The logic is not that simple, but the high level summary is that we store for every tick the liquidity (lots) of positions that have the lower / upper tick here (`lvl.bidLots_`, `lvl.askLots_`). When a tick is then crossed, the whole liquidity is added or removed from `curve.concLiq_`.
>
> However, it can also be easily verified by looking at our test. If the assumption of the warden were true, the user in the test (that has a position with width 30) would not receive 100% of the rewards, but only `1/30`. Because `concLiq_` works this way, the recommendation of the warden would break the system.
> 
> Something that is true is point 1 from [#98](https://github.com/code-423n4/2023-10-canto-findings/issues/98). If a user has a very narrow position (less than 21 ticks), it still contributes to `curve.concLiq_`.

**[LSDan (judge) commented](https://github.com/code-423n4/2023-10-canto-findings/issues/177#issuecomment-1768244629):**
 > TL;DR - in some cases reward amounts may be miscalculated, resulting in lower than expected reward amounts.

***

# Low Risk and Non-Critical Issues

For this audit, 37 reports were submitted by wardens detailing low risk and non-critical issues. The [report highlighted below](https://github.com/code-423n4/2023-10-canto-findings/issues/264) by **adriro** received the top score from the judge.

*The following wardens also submitted reports: [radev\_sw](https://github.com/code-423n4/2023-10-canto-findings/issues/297), [albahaca](https://github.com/code-423n4/2023-10-canto-findings/issues/137), [MatricksDeCoder](https://github.com/code-423n4/2023-10-canto-findings/issues/32), [JP\_Courses](https://github.com/code-423n4/2023-10-canto-findings/issues/306), [0xDING99YA](https://github.com/code-423n4/2023-10-canto-findings/issues/294), [0xdice91](https://github.com/code-423n4/2023-10-canto-findings/issues/279), [Mike\_Bello90](https://github.com/code-423n4/2023-10-canto-findings/issues/269), [0xTheC0der](https://github.com/code-423n4/2023-10-canto-findings/issues/244), [Eurovickk](https://github.com/code-423n4/2023-10-canto-findings/issues/242), [marqymarq10](https://github.com/code-423n4/2023-10-canto-findings/issues/231), [orion](https://github.com/code-423n4/2023-10-canto-findings/issues/220), [sces60107](https://github.com/code-423n4/2023-10-canto-findings/issues/210), [wahedtalash77](https://github.com/code-423n4/2023-10-canto-findings/issues/206), [xAriextz](https://github.com/code-423n4/2023-10-canto-findings/issues/185), [BoRonGod](https://github.com/code-423n4/2023-10-canto-findings/issues/180), [gzeon](https://github.com/code-423n4/2023-10-canto-findings/issues/174), [SovaSlava](https://github.com/code-423n4/2023-10-canto-findings/issues/162), [matrix\_0wl](https://github.com/code-423n4/2023-10-canto-findings/issues/150), [3docSec](https://github.com/code-423n4/2023-10-canto-findings/issues/148), [taner2344](https://github.com/code-423n4/2023-10-canto-findings/issues/123), [Topmark](https://github.com/code-423n4/2023-10-canto-findings/issues/122), [0x3b](https://github.com/code-423n4/2023-10-canto-findings/issues/119), [cookedcookee](https://github.com/code-423n4/2023-10-canto-findings/issues/111), [HChang26](https://github.com/code-423n4/2023-10-canto-findings/issues/110), [100su](https://github.com/code-423n4/2023-10-canto-findings/issues/105), [zpan](https://github.com/code-423n4/2023-10-canto-findings/issues/104), [GKBG](https://github.com/code-423n4/2023-10-canto-findings/issues/90), [BRONZEDISC](https://github.com/code-423n4/2023-10-canto-findings/issues/89), [lukejohn](https://github.com/code-423n4/2023-10-canto-findings/issues/81), [IceBear](https://github.com/code-423n4/2023-10-canto-findings/issues/75), [hunter\_w3b](https://github.com/code-423n4/2023-10-canto-findings/issues/71), [0xAadi](https://github.com/code-423n4/2023-10-canto-findings/issues/65), [pep7siup](https://github.com/code-423n4/2023-10-canto-findings/issues/64), [kutugu](https://github.com/code-423n4/2023-10-canto-findings/issues/61), [tpiliposian](https://github.com/code-423n4/2023-10-canto-findings/issues/40), and [0xWaitress](https://github.com/code-423n4/2023-10-canto-findings/issues/9).*

## Low Issue Summary

|ID|Issue|
|:--:|:---|
| [L-01] | `claimConcentratedRewards()` and `claimAmbientRewards()` should be an internal function |
| [L-02] | Governance check is commented out |
| [L-03] | Rewards can be unintentionally overridden |
| [L-04] | Unused rewards cannot be claimed back |
| [L-05] | Missing week validation while claiming rewards |

## Non Critical Issue Summary

|ID|Issue|
|:--:|:---|
| [N-01] | Use Solidity time units |

## Low Issues

## [L-01] `claimConcentratedRewards()` and `claimAmbientRewards()` should be an internal function

- https://github.com/code-423n4/2023-10-canto/blob/main/canto_ambient/contracts/callpaths/LiquidityMiningPath.sol#L54
- https://github.com/code-423n4/2023-10-canto/blob/main/canto_ambient/contracts/callpaths/LiquidityMiningPath.sol#L61

Both of these functions present in the `LiquidityMiningPath` contract are intended to be called via user commands, whose entry point is the `userCmd()` function.

Consider changing the visibility of `claimConcentratedRewards()` and `claimAmbientRewards()` to internal or private.

## [L-02] Governance check is commented out

- https://github.com/code-423n4/2023-10-canto/blob/main/canto_ambient/contracts/callpaths/LiquidityMiningPath.sol#L66
- https://github.com/code-423n4/2023-10-canto/blob/main/canto_ambient/contracts/callpaths/LiquidityMiningPath.sol#L75

Both `setConcRewards()` and `setAmbRewards()` have a privilege check that is commented out and currently ignored:

```solidity
// require(msg.sender == governance_, "Only callable by governance");
```

These functions are called as protocol commands, which undergo a privilege check in the entry point (see [here](https://github.com/code-423n4/2023-10-canto/blob/main/canto_ambient/contracts/CrocSwapDex.sol#L104)), hence the low severity of this issue. 

However, it is not clear if there's a missing additional check to ensure these are called by the governance. Consider either removing the lines or un-commenting the check.

## [L-03] Rewards can be unintentionally overridden

- https://github.com/code-423n4/2023-10-canto/blob/main/canto_ambient/contracts/callpaths/LiquidityMiningPath.sol#L65
- https://github.com/code-423n4/2023-10-canto/blob/main/canto_ambient/contracts/callpaths/LiquidityMiningPath.sol#L74

Lidiquity mining rewards are set up using `setConcRewards()` or `setAmbRewards()`. In both cases, the rewards are overridden instead of accumulated. Taking `setConcRewards()` as the [example](https://github.com/code-423n4/2023-10-canto/blob/main/canto_ambient/contracts/callpaths/LiquidityMiningPath.sol#L65-L72):

```solidity
65:     function setConcRewards(bytes32 poolIdx, uint32 weekFrom, uint32 weekTo, uint64 weeklyReward) public payable {
66:         // require(msg.sender == governance_, "Only callable by governance");
67:         require(weekFrom % WEEK == 0 && weekTo % WEEK == 0, "Invalid weeks");
68:         while (weekFrom <= weekTo) {
69:             concRewardPerWeek_[poolIdx][weekFrom] = weeklyReward;
70:             weekFrom += uint32(WEEK);
71:         }
72:     }
```

Line 69 assigns the new value `weeklyReward` to the storage mapping. If rewards were already set for this pool, i.e. `concRewardPerWeek_[poolIdx][weekFrom] != 0`, then the new assignment will override the existing value.

## [L-04] Unused rewards cannot be claimed back

Although highly unlikely, there is no provided mechanism to claim back unused rewards assigned to periods of time of inactivity in the pool.

## [L-05] Missing week validation while claiming rewards

- https://github.com/code-423n4/2023-10-canto/blob/main/canto_ambient/contracts/mixins/LiquidityMining.sol#L156
- https://github.com/code-423n4/2023-10-canto/blob/main/canto_ambient/contracts/mixins/LiquidityMining.sol#L256

In `claimConcentratedRewards()` and `claimAmbientRewards()`, the implementation takes an array of the weeks which are expected to be claimed. This is user input, and lacks any validation over the provided argument values.

Using `claimConcentratedRewards()` as the example, we can see each element in `weeksToClaim` is not checked to be an actual _week_, i.e. that `week % WEEK == 0`.

```solidity
174:         for (uint256 i; i < weeksToClaim.length; ++i) {
175:             uint32 week = weeksToClaim[i];
176:             require(week + WEEK < block.timestamp, "Week not over yet");
177:             require(
178:                 !concLiquidityRewardsClaimed_[poolIdx][posKey][week],
179:                 "Already claimed"
180:             );
181:             uint256 overallInRangeLiquidity = timeWeightedWeeklyGlobalConcLiquidity_[poolIdx][week];
```

Consider adding an explicit check to ensure the elements in `weeksToClaim` are valid weeks.

```diff
    uint32 week = weeksToClaim[i];
    require(week + WEEK < block.timestamp, "Week not over yet");
+   require(week % WEEK == 0, "Invalid week");
```

## Non Critical Issues

## [N-01] Use Solidity time units

- https://github.com/code-423n4/2023-10-canto/blob/main/canto_ambient/contracts/mixins/LiquidityMining.sol#L13

Instead of defining spans of time manually using seconds, consider using Solidity built-in [time units](https://docs.soliditylang.org/en/v0.8.21/units-and-global-variables.html#time-units).

**[OpenCoreCH (Canto) confirmed](https://github.com/code-423n4/2023-10-canto-findings/issues/264#issuecomment-1761330903)**

**[LSDan (judge) commented](https://github.com/code-423n4/2023-10-canto-findings/issues/264#issuecomment-1771375611):**
 > I agree with all reported issues and their severity.

***

# Gas Optimizations

For this audit, 16 reports were submitted by wardens detailing gas optimizations. The [report highlighted below](https://github.com/code-423n4/2023-10-canto-findings/issues/293) by **niser93** received the top score from the judge.

*The following wardens also submitted reports: [0xAnah](https://github.com/code-423n4/2023-10-canto-findings/issues/282), [JCK](https://github.com/code-423n4/2023-10-canto-findings/issues/258), [hihen](https://github.com/code-423n4/2023-10-canto-findings/issues/233), [naman1778](https://github.com/code-423n4/2023-10-canto-findings/issues/307), [SAQ](https://github.com/code-423n4/2023-10-canto-findings/issues/291), [SY\_S](https://github.com/code-423n4/2023-10-canto-findings/issues/281), [tabriz](https://github.com/code-423n4/2023-10-canto-findings/issues/278), [shamsulhaq123](https://github.com/code-423n4/2023-10-canto-findings/issues/168), [pipidu83](https://github.com/code-423n4/2023-10-canto-findings/issues/147), [Raihan](https://github.com/code-423n4/2023-10-canto-findings/issues/141), [lsaudit](https://github.com/code-423n4/2023-10-canto-findings/issues/92), [hunter\_w3b](https://github.com/code-423n4/2023-10-canto-findings/issues/70), [MatricksDeCoder](https://github.com/code-423n4/2023-10-canto-findings/issues/49), [Polaris\_tow](https://github.com/code-423n4/2023-10-canto-findings/issues/42), and [debo](https://github.com/code-423n4/2023-10-canto-findings/issues/19).*

## Gas Optimizations

| ID | Issue | Instances | Total Gas Saved |
|:-----:|:------|:-------:|:-------------:|
| [G-01] | Remove ternary operator in order to use unchecked and `>=` instead of `<` | 1 | 4526 |
| [G-02] | State variable read in a loop | 5 | 1908 |
| [G-03] | Using ternary operator instead of `if/else` | 1 | 1896 |
| [G-04] | Using a positive conditional flow to save a NOT opcode | 1 | 2750 |

Total: 8 instances over 4 issues with **11080 gas** saved.

Gas totals are estimates using `npx hardhat test` and `hardhat-gas-reporter`.

## [G-01] Remove ternary operator in order to use unchecked and `>=` instead of `<`

Estimated saving:
| Method call or Contract deployment | Before | After | After - Before | (After - Before) / Before |
| :- | :-: | :-: | :-: | :-: |
| `LiquidityMiningPath` | 1540432 | 1535906 | -4526 | -0.29% |

There is 1 instance of this issue:

[[53-57](https://github.com/code-423n4/2023-10-canto/blob/40edbe0c9558b478c84336aaad9b9626e5d99f34/canto_ambient/contracts/mixins/LiquidityMining.sol#L53-L57)]             

```diff
File: LiquidityMining.sol

-   uint32 dt = uint32(
-       nextWeek < block.timestamp
-           ? nextWeek - time
-           : block.timestamp - time
-   );
+   uint32 dt;
+   if(nextWeek >= block.timestamp) {
+       unchecked{dt = uint32(block.timestamp - time);}
+   }
+   else{
+       unchecked{dt = uint32(nextWeek - time);}
+   }

```

## [G-02] State variable read in a loop

The state variable should be cached in a local variable rather than reading it on every iteration of the `for-loop`, which will replace each Gwarmaccess (**100 gas**) with a much cheaper stack read.

Estimated saving:
| Method call or Contract deployment | Before | After | After - Before | (After - Before) / Before |
| :- | :-: | :-: | :-: | :-: |
| `LiquidityMiningPath` | 1540432 | 1538524 | -1908 | -0.12% |

There are 5 instances of this issue:

[[87-97](https://github.com/code-423n4/2023-10-canto/blob/29c92a926453a49c8935025a4d3de449150fc2ff/canto_ambient/contracts/mixins/LiquidityMining.sol#L87-L97)]

```diff
File: LiquidityMining.sol

    uint256 liquidity = pos.liquidity_;
+   uint256 wweek = WEEK;
    for (int24 i = lowerTick + 10; i <= upperTick - 10; ++i) {
        uint32 tickTrackingIndex = tickTrackingIndexAccruedUpTo_[poolIdx][posKey][i];
        uint32 origIndex = tickTrackingIndex;
        uint32 numTickTracking = uint32(tickTracking_[poolIdx][i].length);
        uint32 time = lastAccrued;
        // Loop through all in-range time spans for the tick or up to the current time (if it is still in range)
        while (time < block.timestamp && tickTrackingIndex < numTickTracking) {
            TickTracking memory tickTracking = tickTracking_[poolIdx][i][tickTrackingIndex];
-              uint32 currWeek = uint32((time / WEEK) * WEEK);
-              uint32 nextWeek = uint32(((time + WEEK) / WEEK) * WEEK);
+               uint32 currWeek = uint32((time / WEEK) * WEEK);
+               uint32 nextWeek = uint32(((time + WEEK) / WEEK) * WEEK);
```

## [G-03] Using ternary operator instead of `if/else`

Estimated saving:
| Method call or Contract deployment | Before | After | After - Before | (After - Before) / Before |
| :- | :-: | :-: | :-: | :-: |
| `LiquidityMiningPath` | 1540432 | 1538536 | -1896 | -0.12% |

There is 1 instance of this issue:

[[53-57](https://github.com/code-423n4/2023-10-canto/blob/40edbe0c9558b478c84336aaad9b9626e5d99f34/canto_ambient/contracts/mixins/LiquidityMining.sol#L53-L57)]

```diff
File: LiquidityMining.sol

-   if (tickTracking.enterTimestamp < time) {
-       // Tick was already active when last claim happened, only accrue from last claim timestamp
-       tickActiveStart = time;
-   } else {
-       // Tick has become active this week
-       tickActiveStart = tickTracking.enterTimestamp;
-   }
+   tickActiveStart = tickTracking.enterTimestamp >= time ? time : tickTracking.enterTimestamp;
```

## [G-04] Using a positive conditional flow to save a NOT opcode

In order to save some gas (NOT opcode costing 3 gas), switch to a positive statement:

```diff
- if(!condition){
-     action1();
- }else{
-     action2();
- }
+ if(condition){
+     action2();
+ }else{
+     action1();
+ }
```            

Estimated saving:
| Method call or Contract deployment | Before | After | After - Before | (After - Before) / Before |
| :- | :-: | :-: | :-: | :-: |
| `LiquidityMiningPath` | 1540432 | 1537682 | -2750 | -0.18% |

There is 1 instance of this issue:

[[86-150](https://github.com/code-423n4/2023-10-canto/blob/main/canto_ambient/contracts/mixins/LiquidityMining.sol#L86-L150)]

<details>

```
File: LiquidityMining.sol


  86           if (lastAccrued != 0) {
  87               uint256 liquidity = pos.liquidity_;
  88               for (int24 i = lowerTick + 10; i <= upperTick - 10; ++i) {
  89                   uint32 tickTrackingIndex = tickTrackingIndexAccruedUpTo_[poolIdx][posKey][i];
  90                   uint32 origIndex = tickTrackingIndex;
  91                   uint32 numTickTracking = uint32(tickTracking_[poolIdx][i].length);
  92                   uint32 time = lastAccrued;
  93                   // Loop through all in-range time spans for the tick or up to the current time (if it is still in range)
  94                   while (time < block.timestamp && tickTrackingIndex < numTickTracking) {
  95                       TickTracking memory tickTracking = tickTracking_[poolIdx][i][tickTrackingIndex];
  96                       uint32 currWeek = uint32((time / WEEK) * WEEK);
  97                       uint32 nextWeek = uint32(((time + WEEK) / WEEK) * WEEK);
  98                       uint32 dt = uint32(
  99                           nextWeek < block.timestamp
  100                              ? nextWeek - time
  101                              : block.timestamp - time
  102                      );
  103                      uint32 tickActiveStart; // Timestamp to use for the liquidity addition
  104                      uint32 tickActiveEnd;
  105                      if (tickTracking.enterTimestamp < nextWeek) {
  106                          // Tick was active before next week, need to add the liquidity
  107                          if (tickTracking.enterTimestamp < time) {
  108                              // Tick was already active when last claim happened, only accrue from last claim timestamp
  109                              tickActiveStart = time;
  110                          } else {
  111                              // Tick has become active this week
  112                              tickActiveStart = tickTracking.enterTimestamp;
  113                          }
  114                          if (tickTracking.exitTimestamp == 0) {
  115                              // Tick still active, do not increase index because we need to continue from here
  116                              tickActiveEnd = uint32(nextWeek < block.timestamp ? nextWeek : block.timestamp);
  117                          } else {
  118                              // Tick is no longer active
  119                              if (tickTracking.exitTimestamp < nextWeek) {
  120                                  // Exit was in this week, continue with next tick
  121                                  tickActiveEnd = tickTracking.exitTimestamp;
  122                                  tickTrackingIndex++;
  123                                  dt = tickActiveEnd - tickActiveStart;
  124                              } else {
  125                                  // Exit was in next week, we need to consider the current tick there (i.e. not increase the index)
  126                                  tickActiveEnd = nextWeek;
  127                              }
  128                          }
  129                          timeWeightedWeeklyPositionInRangeConcLiquidity_[poolIdx][posKey][currWeek][i] +=
  130                              (tickActiveEnd - tickActiveStart) * liquidity;
  131                      }
  132                      time += dt;
  133                  }
  134                  if (tickTrackingIndex != origIndex) {
  135                      tickTrackingIndexAccruedUpTo_[poolIdx][posKey][i] = tickTrackingIndex;
  136                  }
  137              }
  138          } else {
  139              for (int24 i = lowerTick + 10; i <= upperTick - 10; ++i) {
  140                  uint32 numTickTracking = uint32(tickTracking_[poolIdx][i].length);
  141                  if (numTickTracking > 0) {
  142                      if (tickTracking_[poolIdx][i][numTickTracking - 1].exitTimestamp == 0) {
  143                          // Tick currently active
  144                          tickTrackingIndexAccruedUpTo_[poolIdx][posKey][i] = numTickTracking - 1;
  145                      } else {
  146                          tickTrackingIndexAccruedUpTo_[poolIdx][posKey][i] = numTickTracking;
  147                      }
  148                  }
  149              }
  150          }
```

```diff
File: LiquidityMining.sol

-   86           if (lastAccrued != 0) {
-   87               uint256 liquidity = pos.liquidity_;
-   88               for (int24 i = lowerTick + 10; i <= upperTick - 10; ++i) {
-   89                   uint32 tickTrackingIndex = tickTrackingIndexAccruedUpTo_[poolIdx][posKey][i];
-   90                   uint32 origIndex = tickTrackingIndex;
-   91                   uint32 numTickTracking = uint32(tickTracking_[poolIdx][i].length);
-   92                   uint32 time = lastAccrued;
-   93                   // Loop through all in-range time spans for the tick or up to the current time (if it is still in range)
-   94                   while (time < block.timestamp && tickTrackingIndex < numTickTracking) {
-   95                       TickTracking memory tickTracking = tickTracking_[poolIdx][i][tickTrackingIndex];
-   96                       uint32 currWeek = uint32((time / WEEK) * WEEK);
-   97                       uint32 nextWeek = uint32(((time + WEEK) / WEEK) * WEEK);
-   98                       uint32 dt = uint32(
-   99                           nextWeek < block.timestamp
-   100                              ? nextWeek - time
-   101                              : block.timestamp - time
-   102                      );
-   103                      uint32 tickActiveStart; // Timestamp to use for the liquidity addition
-   104                      uint32 tickActiveEnd;
-   105                      if (tickTracking.enterTimestamp < nextWeek) {
-   106                          // Tick was active before next week, need to add the liquidity
-   107                          if (tickTracking.enterTimestamp < time) {
-   108                              // Tick was already active when last claim happened, only accrue from last claim timestamp
-   109                              tickActiveStart = time;
-   110                          } else {
-   111                              // Tick has become active this week
-   112                              tickActiveStart = tickTracking.enterTimestamp;
-   113                          }
-   114                          if (tickTracking.exitTimestamp == 0) {
-   115                              // Tick still active, do not increase index because we need to continue from here
-   116                              tickActiveEnd = uint32(nextWeek < block.timestamp ? nextWeek : block.timestamp);
-   117                          } else {
-   118                              // Tick is no longer active
-   119                              if (tickTracking.exitTimestamp < nextWeek) {
-   120                                  // Exit was in this week, continue with next tick
-   121                                  tickActiveEnd = tickTracking.exitTimestamp;
-   122                                  tickTrackingIndex++;
-   123                                  dt = tickActiveEnd - tickActiveStart;
-   124                              } else {
-   125                                  // Exit was in next week, we need to consider the current tick there (i.e. not increase the index)
-   126                                  tickActiveEnd = nextWeek;
-   127                              }
-   128                          }
-   129                          timeWeightedWeeklyPositionInRangeConcLiquidity_[poolIdx][posKey][currWeek][i] +=
-   130                              (tickActiveEnd - tickActiveStart) * liquidity;
-   131                      }
-   132                      time += dt;
-   133                  }
-   134                  if (tickTrackingIndex != origIndex) {
-   135                      tickTrackingIndexAccruedUpTo_[poolIdx][posKey][i] = tickTrackingIndex;
-   136                  }
-   137              }
-   138          } else {
-   139              for (int24 i = lowerTick + 10; i <= upperTick - 10; ++i) {
-   140                  uint32 numTickTracking = uint32(tickTracking_[poolIdx][i].length);
-   141                  if (numTickTracking > 0) {
-   142                      if (tickTracking_[poolIdx][i][numTickTracking - 1].exitTimestamp == 0) {
-   143                          // Tick currently active
-   144                          tickTrackingIndexAccruedUpTo_[poolIdx][posKey][i] = numTickTracking - 1;
-   145                      } else {
-   146                          tickTrackingIndexAccruedUpTo_[poolIdx][posKey][i] = numTickTracking;
-   147                      }
-   148                  }
-   149              }
-   150          }


+   86             if (lastAccrued == 0) {
+   87                 for (int24 i = lowerTick + 10; i <= upperTick - 10; ++i) {
+   88                     uint32 numTickTracking = uint32(tickTracking_[poolIdx][i].length);
+   89                     if (numTickTracking > 0) {
+   90                         if (tickTracking_[poolIdx][i][numTickTracking - 1].exitTimestamp == 0) {
+   91                             // Tick currently active
+   92                             tickTrackingIndexAccruedUpTo_[poolIdx][posKey][i] = numTickTracking - 1;
+   93                         } else {
+   94                             tickTrackingIndexAccruedUpTo_[poolIdx][posKey][i] = numTickTracking;
+   95                         }
+   96                     }
+   97                 }
+   98             } else {
+   99                 uint256 liquidity = pos.liquidity_;
+   100                 for (int24 i = lowerTick + 10; i <= upperTick - 10; ++i) {
+   101                     uint32 tickTrackingIndex = tickTrackingIndexAccruedUpTo_[poolIdx][posKey][i];
+   102                     uint32 origIndex = tickTrackingIndex;
+   103                     uint32 numTickTracking = uint32(tickTracking_[poolIdx][i].length);
+   104                     uint32 time = lastAccrued;
+   105                     // Loop through all in-range time spans for the tick or up to the current time (if it is still in range)
+   106                     while (time < block.timestamp && tickTrackingIndex < numTickTracking) {
+   107                         TickTracking memory tickTracking = tickTracking_[poolIdx][i][tickTrackingIndex];
+   108                         uint32 currWeek = uint32((time / WEEK) * WEEK);
+   109                         uint32 nextWeek = uint32(((time + WEEK) / WEEK) * WEEK);
+   110                         uint32 dt = uint32(
+   111                             nextWeek < block.timestamp
+   112                                 ? nextWeek - time
+   113                                 : block.timestamp - time
+   114                         );
+   115                         uint32 tickActiveStart; // Timestamp to use for the liquidity addition
+   116                         uint32 tickActiveEnd;
+   117                         if (tickTracking.enterTimestamp < nextWeek) {
+   118                             // Tick was active before next week, need to add the liquidity
+   119                             if (tickTracking.enterTimestamp < time) {
+   120                                 // Tick was already active when last claim happened, only accrue from last claim timestamp
+   121                                 tickActiveStart = time;
+   122                             } else {
+   123                                 // Tick has become active this week
+   124                                 tickActiveStart = tickTracking.enterTimestamp;
+   125                             }
+   126                             if (tickTracking.exitTimestamp == 0) {
+   127                                 // Tick still active, do not increase index because we need to continue from here
+   128                                 tickActiveEnd = uint32(nextWeek < block.timestamp ? nextWeek : block.timestamp);
+   129                             } else {
+   130                                 // Tick is no longer active
+   131                                 if (tickTracking.exitTimestamp < nextWeek) {
+   132                                     // Exit was in this week, continue with next tick
+   133                                     tickActiveEnd = tickTracking.exitTimestamp;
+   134                                     tickTrackingIndex++;
+   135                                     dt = tickActiveEnd - tickActiveStart;
+   136                                 } else {
+   137                                     // Exit was in next week, we need to consider the current tick there (i.e. not increase the index)
+   138                                     tickActiveEnd = nextWeek;
+   139                                 }
+   140                             }
+   141                             timeWeightedWeeklyPositionInRangeConcLiquidity_[poolIdx][posKey][currWeek][i] +=
+   142                                 (tickActiveEnd - tickActiveStart) * liquidity;
+   143                         }
+   144                         time += dt;
+   145                     }
+   146                     if (tickTrackingIndex != origIndex) {
+   147                         tickTrackingIndexAccruedUpTo_[poolIdx][posKey][i] = tickTrackingIndex;
+   148                     }
+   149                 }
+   150             }
```

</details>

***

# Audit Analysis

For this audit, 11 analysis reports were submitted by wardens. An analysis report examines the codebase as a whole, providing observations and advice on such topics as architecture, mechanism, or approach. The [report highlighted below](https://github.com/code-423n4/2023-10-canto-findings/issues/230) by **0xweb3boy** received the top score from the judge.

*The following wardens also submitted reports: [hunter\_w3b](https://github.com/code-423n4/2023-10-canto-findings/issues/72), [sandy](https://github.com/code-423n4/2023-10-canto-findings/issues/304), [0xdice91](https://github.com/code-423n4/2023-10-canto-findings/issues/300), [radev\_sw](https://github.com/code-423n4/2023-10-canto-findings/issues/299), [Banditx0x](https://github.com/code-423n4/2023-10-canto-findings/issues/275), [JP\_Courses](https://github.com/code-423n4/2023-10-canto-findings/issues/184), [ZanyBonzy](https://github.com/code-423n4/2023-10-canto-findings/issues/121), [cookedcookee](https://github.com/code-423n4/2023-10-canto-findings/issues/120), [albahaca](https://github.com/code-423n4/2023-10-canto-findings/issues/118), and [invitedtea](https://github.com/code-423n4/2023-10-canto-findings/issues/85).*

## Table of Contents

1. Executive Summary<br>
2. Code Audit Approach<br>
    2.1 Audit Documentation and Scope<br>
    2.2 Code review<br>
    2.3 Threat Modelling<br>
    2.4 Exploitation and Proofs of Concept<br>
    2.5 Report Issues<br>
3. Architecture overview<br>
    3.1 Overview of Liquidity Mining Feature by Canto for Ambient Finance<br>
    3.2  Key Contracts Introduced<br>
    3.3 Incentive Mechanism<br>
    3.4 Liquidity Mining Rewards<br>
    3.5 Reward Distribution Example<br>
    3.6 Setting Weekly Reward Rate<br>
4. Implementation Notes<br>
    4.1 General Impressions<br>
    4.2 Composition over Inheritance<br>
    4.3 Comments<br>
    4.4 Solidity Versions<br>
5. Conclusion

## 1. Executive Summary

In focusing on the ongoing audit 2023-10-canto, my analysis starts by delineating the code audit methodology applied to the contracts within the defined scope. Subsequently, I provided insights into the architectural aspects, offering my perspective. Finally, I offered observations pertaining to the code implementation.

I want to emphasize that unless expressly specified, any potential architectural risks or implementation concerns discussed in this document should not be construed as vulnerabilities or suggestions to modify the architecture or code based solely on this analysis. As an auditor, I recognize the necessity of a comprehensive evaluation of design choices in intricate projects, considering risks as only one component of a larger evaluative process. It's essential to acknowledge that the project team may have already evaluated these risks and established the most appropriate approach to mitigate or coexist with them.

## 2. Code Audit Approach

### 2.1 Audit Documentation and Scope
Commencing the analysis, the first phase entailed a thorough review of the [repo](https://github.com/code-423n4/2023-10-canto/tree/main) to fully grasp the fundamental concepts and limitations of the audit. This initial step was crucial in guiding the prioritization of my audit efforts. Notably, the README associated with this audit stands out for its excellent quality, offering valuable insights and actionable guidance that significantly streamline the onboarding process for auditors.

### 2.2 Code review

Initiating the code review, the starting point involved gaining a comprehensive understanding of "LiquidityMining.sol," a pivotal component responsible for implementing a liquidity mining protocol for Ambient. Canto's strategic intention is to leverage this sidecar mechanism to incentivize liquidity provision for Ambient pools deployed on their platform. This understanding of the core pattern significantly facilitated the comprehension of the protocol contracts and their interconnections. During this phase, meticulous documentation of observations and the formulation of pertinent questions regarding potential exploits were undertaken, striking a balance between depth and breadth of analysis.

### 2.3 Threat Modelling

The initial step involved crafting precise assumptions that, if breached, could present notable security risks to the system. This approach serves to guide the identification of optimal exploitation strategies. Although not an exhaustive threat modeling exercise, it closely aligns with the essence of such an analysis.

### 2.4 Exploitation and Proofs of Concept

Progressing from this juncture, the primary methodology took the form of a cyclic process, conditionally encompassing steps 2.2, 2.3, and 2.4. This involved iterative attempts at exploitation and the subsequent creation of proofs of concept, occasionally aided by available documentation or the helpful community on Discord. The key focus during this phase was to challenge fundamental assumptions, generate novel ones in the process, and refine the approach by utilizing coded proofs of concept to hasten the development of successful exploits.

### 2.5 Report Issues

While this particular stage might initially appear straightforward, it harbors subtleties worth considering. Hastily reporting vulnerabilities and subsequently overlooking them is not a prudent course of action. The optimal approach to augment the value delivered to sponsors (and ideally, to auditors as well) entails thoroughly documenting the potential gains from exploiting each vulnerability. This comprehensive assessment aids in the determination of whether these exploits could be strategically amalgamated to generate a more substantial impact on the system's security. It's important to recognize that seemingly minor and moderate issues, when skillfully leveraged, can compound into a critical vulnerability. This assessment must be weighed against the risks that users might encounter. Within the realm of Code4rena audits, a heightened level of caution and an expedited reporting channel are accorded to zero-day vulnerabilities or highly sensitive bugs impacting deployed contracts.

## 3. Architecture overview

### 3.1 Overview of Liquidity Mining Feature by Canto for Ambient Finance
Introduction to the Feature: Canto, in its pursuit of enhancing liquidity dynamics, has introduced a new liquidity mining feature tailored specifically for Ambient Finance, a targeted approach to bolster the platform's liquidity infrastructure.

Integration through Sidecar Contract: The implementation strategy involves the creation of a sidecar contract meticulously designed to integrate into the Ambient ecosystem. This integration is achieved through the utilization of Ambient's proxy contract pattern, a structured approach to seamlessly amalgamate the new liquidity mining feature.

### 3.2 Key Contracts Introduced

LiquidityMiningPath.sol: This contract is pivotal in providing the essential interfaces, enabling seamless interactions for users interacting with the liquidity mining protocol.

LiquidityMining.sol: This contract forms the operational backbone, encapsulating the logic and functionalities necessary for the effective operation of the liquidity mining feature.

**Understanding the LiquidityMining Sidecar**<br>
Objective of the Sidecar: The LiquidityMining sidecar is meticulously engineered to realize a robust liquidity mining protocol within the Ambient ecosystem. Canto envisions utilizing this sidecar to stimulate and incentivize liquidity contributions to the Ambient pools hosted on Canto's platform.

### 3.3 Incentive Mechanism

The sidecar employs an incentivization mechanism targeting a specific width of liquidity, primarily based on the current tick. Focused on stabilizing liquidity pools, the incentivization range spans from the current tick minus 10 to the current tick plus 10.

To qualify for incentives, a user's liquidity range must encompass at least 21 ticks, inclusive of the current tick and 10 ticks on each side.
Additionally, users are advised to maintain a slight buffer on either side of the stipulated range to ensure uninterrupted rewards, particularly in response to minor price fluctuations.

### 3.4 Liquidity Mining Rewards

The core idea behind the liquidity mining sidecar centers on tracking the time-weighted liquidity across global and per-user levels.
This tracking is conducted for both ambient and concentrated positions on a per-tick basis.

The protocol calculates the user's proportion of in-range liquidity over a specific time span, subsequently disbursing this percentage of the global rewards to the user.

### 3.5 Reward Distribution Example

For illustrative purposes, if the weekly rewards amount to 10 CANTO and only LP A is contributing liquidity, "LP A" will receive the entire 10 CANTO as their reward. However, if there are multiple liquidity providers, such as "LP A" and "LP B", who contribute liquidity throughout the week, the rewards will be shared evenly. In this scenario, each provider will receive 5 CANTO.
Implementation Insights

### 3.6 Setting Weekly Reward Rate

The liquidity mining sidecar incorporates functions dedicated to setting the weekly reward rate. The reward rates are determined by establishing a total disbursement amount per week, providing the governing body the flexibility to choose the number of weeks for which the reward rate will be set.

Focus on LiquidityMining.sol: The critical aspect of the implementation lies within the LiquidityMining.sol contract, housing the core logic for reward accumulation and claim processes. Auditors and wardens are strongly advised to direct their primary focus towards this segment of the codebase, recognizing its pivotal role in the successful operation of the liquidity mining feature.

## 4. Implementation Notes

During the course of the audit, several noteworthy implementation details were identified, and among these, a significant subset holds potential value for the ongoing analysis.

### 4.1 General Impressions

**Overview of Ambient**

Ambient Finance: Ambient is a single-contract decentralized exchange (dex) designed to facilitate liquidity provision in a flexible manner. It allows liquidity providers to deposit liquidity in either the "ambient" style (similar to uniV2) or the "concentrated" style (similar to uniV3) into any token pair.

Main Contract: The primary contract in Ambient Finance is called `CrocSwapDex`. Users interact with this contract, and it is the main interface for all actions related to the protocol.

**Sidecar Contracts**

Ambient utilizes modular proxy contracts called "sidecars," each responsible for a unique function within the protocol.

Here are the sidecar contracts:
- BootPath: Special sidecar used to install other sidecar contracts.
- ColdPath: Handles the creation of new pools.
- WarmPath: Manages liquidity operations like minting and burning.
- LiquidityMiningPath: New sidecar developed by Canto to handle liquidity mining for both ambient and concentrated liquidity.
- KnockoutPath: Manages logic for knockout liquidity.
- LongPath: Contains logic for parsing and executing arbitrarily long compound orders.
- MicroPaths: Contains functions related to single atomic actions within a longer compound action on a pre-loaded pool's liquidity curve.
- SafeModePath: Reserved for emergency mode.

**Interacting with Ambient Contracts**

User and Protocol Commands: Interaction with Ambient contracts is facilitated through two main functions:
- `userCmd(uint16 callpath, bytes calldata cmd)`: Used by users for various actions.
- `protocolCmd(uint16 callpath, bytes calldata cmd, bool sudo)`: Utilized for governance-related actions.

`Callpath Parameter`: The callpath parameter determines which sidecar contract receives the command. Different values correspond to different sidecar contracts, each serving a specific purpose.

`Command Encoding (cmd)`: The cmd parameter is ABI encoded calldata fed to the specified sidecar contract. The code parameter within cmd specifies the function to be called within the sidecar contract based on the desired action.

### 4.2 Composition over Inheritance

Canto has used inheritance over composition because inheritance is a  prevalent choice due to the need for standardized behaviors and code reusability. Smart contracts often adhere to established standards such as ERC-20 or ERC-721, and inheritance facilitates the straightforward integration of these standards, promoting interoperability and adherence to well-defined interfaces. By centralizing common functionalities in a base contract and allowing other contracts to inherit these functionalities, developers can streamline deployment, reduce redundancy, and simplify interactions. In addition, this approach aids in efficient gas usage, aligning with the limitations imposed by the Ethereum Virtual Machine (EVM) contract size. Moreover, inheritance supports logical code organization and maintenance, enabling easier updates and enhancing readability by segregating related functionalities into distinct contracts.

### 4.3 Comments

**Importance of Comments for Clarity**

Comments serve a pivotal role in enhancing the understandability of the codebase. While the code is generally clean and logically structured, judiciously placed comments can provide valuable insights into the functionalities and intentions behind the code. They contribute to a better comprehension of the code's purpose, especially for auditors and developers involved in the analysis.

**Strategic Comment Placement**

The codebase would greatly benefit from an increased presence of comments, particularly within the `LiquidityMining.sol` contract. Strategic placement of comments within this essential contract can significantly aid auditors in comprehending the implementation details. These comments should elucidate the logic, processes, and methodologies employed, promoting a seamless audit experience.

**Facilitating Audits and Code Readability**

Comprehensive comments in the `LiquidityMining.sol` contract can expedite the auditing process by allowing auditors to swiftly grasp the intended functionality of the code. This, in turn, enhances the readability of the functions and methods, making it easier for auditors to identify any inconsistencies or deviations between the documented intentions and the actual code implementation.

**Detecting Discrepancies in Code Intentions**

An important aspect of code review is discerning any mismatches between the documented intentions in the comments and the actual code implementation. Comments that accurately reflect the code's purpose are crucial for auditors, as discrepancies between the two can be indicators of potential vulnerabilities or errors. The act of aligning comments with the true code behavior is fundamental to ensuring the reliability and security of the smart contract.

### 4.4 Solidity Versions

Though there are valid arguments both in support of and against adopting the latest Solidity version, I find that this discussion bears little significance for the current state of the project. Without a doubt, choosing the most up-to-date version is a far superior decision when compared to the potential risks associated with outdated versions.

## 5. Conclusion

### Positive Audit Experience

The process of auditing this codebase and evaluating its architectural choices has been thoroughly enjoyable and enriching. Navigating through the intricacies and nuances of the project has been enlightening, presenting an opportunity to delve into the complexities of the system.

### Strategic Simplifications for Complexity Management

Inherent complexity is a characteristic of many systems, especially those in the realm of blockchain and smart contracts. The strategic introduction of simplifications within this project has proven to be a valuable approach. These simplifications are well-thought-out and strategically implemented, demonstrating an understanding of how to manage complexity effectively.

### Achieving a Harmonious Balance

A notable achievement of this project is striking a harmonious balance between the imperative for simplicity and the challenge of managing inherent complexity. This equilibrium is crucial in ensuring that the codebase remains comprehensible, maintainable, and scalable, even as the system becomes more intricate.

### Importance of Methodology Overview

The overview provided regarding the methodology employed during the audit of the contracts within the defined scope is invaluable. It offers a clear and structured insight into the analytical approach undertaken, shedding light on the depth and rigor of the evaluation process.

### Relevance for Project Team and Stakeholders

The insights presented are not only beneficial for the project team but also extend to any party with an interest in analyzing this codebase. The detailed observations, considerations, and recommendations have the potential to guide and inform decision-making, contributing to the project's overall improvement and security.

### Time spent
16 hours

**[OpenCoreCH (Canto) acknowledged](https://github.com/code-423n4/2023-10-canto-findings/issues/230#issuecomment-1757583243)**

***

# Disclosures

C4 is an open organization governed by participants in the community.

C4 Audits incentivize the discovery of exploits, vulnerabilities, and bugs in smart contracts. Security researchers are rewarded at an increasing rate for finding higher-risk issues. Audit submissions are judged by a knowledgeable security researcher and solidity developer and disclosed to sponsoring developers. C4 does not conduct formal verification regarding the provided code but instead provides final verification.

C4 does not provide any guarantee or warranty regarding the security of this project. All smart contract software should be used at the sole risk and responsibility of users.

# Play and Tactic FSM Diagrams

## [PlaySelectionFSM](/src/software/ai/play_selection_fsm.h)

```mermaid

stateDiagram-v2
classDef terminate fill:white,color:black,font-weight:bold
direction LR
[*] --> Halt
Halt --> Stop : [gameStateStopped]\n<i>setupStopPlay</i>
Halt --> Playing : [gameStatePlaying]\n<i>setupOffensePlay</i>
Halt --> SetPlay : [gameStateSetupRestart]\n<i>setupSetPlay</i>
Stop --> Halt : [gameStateHalted]\n<i>setupHaltPlay</i>
Stop --> Playing : [gameStatePlaying]\n<i>setupOffensePlay</i>
Stop --> SetPlay : [gameStateSetupRestart]\n<i>setupSetPlay</i>
Playing --> Halt : [gameStateHalted]\n<i>setupHaltPlay</i>
Playing --> Stop : [gameStateStopped]\n<i>setupStopPlay</i>
Playing --> SetPlay : [gameStateSetupRestart]\n<i>setupSetPlay</i>
SetPlay --> Halt : [gameStateHalted]\n<i>resetSetPlay, setupHaltPlay</i>
SetPlay --> Stop : [gameStateStopped]\n<i>resetSetPlay, setupStopPlay</i>
SetPlay --> Playing : [gameStatePlaying]\n<i>resetSetPlay, setupOffensePlay</i>
SetPlay --> SetPlay : [gameStateSetupRestart]\n<i>setupSetPlay</i>
Terminate:::terminate --> Terminate:::terminate

```

## [BallPlacementPlayFSM](/src/software/ai/hl/stp/play/ball_placement/ball_placement_play_fsm.h)

```mermaid

stateDiagram-v2
classDef terminate fill:white,color:black,font-weight:bold
direction LR
[*] --> StartState
StartState --> AlignPlacementState : [!shouldKickOffWall]\n<i>alignPlacement</i>
StartState --> KickOffWallState : [shouldKickOffWall]
KickOffWallState --> KickOffWallState : [!kickDone && shouldKickOffWall]\n<i>kickOffWall</i>
KickOffWallState --> KickOffWallState : [kickDone]
KickOffWallState --> AlignPlacementState : [!kickDone]
AlignPlacementState --> KickOffWallState : [shouldKickOffWall]
AlignPlacementState --> AlignPlacementState : [!alignDone]\n<i>alignPlacement</i>
AlignPlacementState --> PlaceBallState : [alignDone]
PlaceBallState --> PlaceBallState : [!ballPlaced]\n<i>placeBall</i>
PlaceBallState --> WaitState : [ballPlaced]\n<i>startWait</i>
WaitState --> WaitState : [!waitDone]
WaitState --> RetreatState : [waitDone]
RetreatState --> Terminate:::terminate : [retreatDone && ballPlaced]
RetreatState --> RetreatState : [ballPlaced]\n<i>retreat</i>

```

## [CreaseDefensePlayFSM](/src/software/ai/hl/stp/play/crease_defense/crease_defense_play_fsm.h)

```mermaid

stateDiagram-v2
classDef terminate fill:white,color:black,font-weight:bold
direction LR
[*] --> DefenseState
DefenseState --> DefenseState : <i>defendDefenseArea</i>
Terminate:::terminate --> Terminate:::terminate

```

## [DefensePlayFSM](/src/software/ai/hl/stp/play/defense/defense_play_fsm.h)

```mermaid

stateDiagram-v2
classDef terminate fill:white,color:black,font-weight:bold
direction LR
[*] --> DefenseState
DefenseState --> AggressiveDefenseState : [shouldDefendAggressively]\n<i>shadowAndBlockShots</i>
DefenseState --> DefenseState : <i>blockShots</i>
AggressiveDefenseState --> DefenseState : [!shouldDefendAggressively]\n<i>blockShots</i>
AggressiveDefenseState --> AggressiveDefenseState : <i>shadowAndBlockShots</i>
Terminate:::terminate --> Terminate:::terminate

```

## [EnemyBallPlacementPlayFSM](/src/software/ai/hl/stp/play/enemy_ball_placement/enemy_ball_placement_play_fsm.h)

```mermaid

stateDiagram-v2
classDef terminate fill:white,color:black,font-weight:bold
direction LR
[*] --> WaitState
WaitState --> AvoidState : [hasPlacementPoint]\n<i>setPlacementPoint</i>
WaitState --> WaitState : [!hasPlacementPoint]
AvoidState --> AvoidState : [!isNearlyPlaced]\n<i>avoid</i>
AvoidState --> DefenseState : [isNearlyPlaced]
DefenseState --> DefenseState : [isNearlyPlaced]\n<i>enterDefensiveFormation</i>
DefenseState --> AvoidState : [!isNearlyPlaced]

```

## [EnemyFreeKickPlayFSM](/src/software/ai/hl/stp/play/enemy_free_kick/enemy_free_kick_play_fsm.h)

```mermaid

stateDiagram-v2
classDef terminate fill:white,color:black,font-weight:bold
direction LR
[*] --> BlockEnemyKickerState
BlockEnemyKickerState --> BlockEnemyKickerState : <i>blockEnemyKicker</i>
Terminate:::terminate --> Terminate:::terminate

```

## [ExamplePlayFSM](/src/software/ai/hl/stp/play/example/example_play_fsm.h)

```mermaid

stateDiagram-v2
classDef terminate fill:white,color:black,font-weight:bold
direction LR
[*] --> MoveState
MoveState --> MoveState : <i>moveToPosition</i>
Terminate:::terminate --> Terminate:::terminate

```

## [FreeKickPlayFSM](/src/software/ai/hl/stp/play/free_kick/free_kick_play_fsm.h)

```mermaid

stateDiagram-v2
classDef terminate fill:white,color:black,font-weight:bold
direction LR
[*] --> SetupPositionState
SetupPositionState --> SetupPositionState : [!setupDone]\n<i>setupPosition</i>
SetupPositionState --> ShootState : [shotFound]
ShootState --> ShootState : [!shotDone]\n<i>shootBall</i>
ShootState --> Terminate:::terminate : [shotDone]
SetupPositionState --> AttemptPassState : <i>startLookingForPass</i>
AttemptPassState --> ChipState : [timeExpired]
AttemptPassState --> AttemptPassState : [!passFound]\n<i>lookForPass</i>
AttemptPassState --> PassState : [passFound]
PassState --> AttemptPassState : [shouldAbortPass]
PassState --> PassState : [!passDone]\n<i>passBall</i>
PassState --> Terminate:::terminate : [passDone]
ChipState --> ChipState : [!chipDone]\n<i>chipBall</i>
ChipState --> Terminate:::terminate : [chipDone]

```

## [HaltPlayFSM](/src/software/ai/hl/stp/play/halt_play/halt_play_fsm.h)

```mermaid

stateDiagram-v2
classDef terminate fill:white,color:black,font-weight:bold
direction LR
[*] --> HaltState
HaltState --> HaltState : <i>updateStop</i>
Terminate:::terminate --> Terminate:::terminate : <i>updateStop</i>

```

## [OffensePlayFSM](/src/software/ai/hl/stp/play/offense/offense_play_fsm.h)

```mermaid

stateDiagram-v2
classDef terminate fill:white,color:black,font-weight:bold
direction LR
[*] --> OffensiveState
OffensiveState --> DefensiveState : [enemyHasPossession]\n<i>setupDefensiveStrategy</i>
OffensiveState --> OffensiveState : <i>setupOffensiveStrategy</i>
DefensiveState --> OffensiveState : [!enemyHasPossession]\n<i>setupOffensiveStrategy</i>
DefensiveState --> DefensiveState : <i>setupDefensiveStrategy</i>
Terminate:::terminate --> Terminate:::terminate

```

## [PenaltyKickPlayFSM](/src/software/ai/hl/stp/play/penalty_kick/penalty_kick_play_fsm.h)

```mermaid

stateDiagram-v2
classDef terminate fill:white,color:black,font-weight:bold
direction LR
[*] --> SetupPositionState
SetupPositionState --> SetupPositionState : [!setupPositionDone]\n<i>setupPosition</i>
SetupPositionState --> PerformKickState : [setupPositionDone]
PerformKickState --> PerformKickState : [!kickDone]\n<i>performKick</i>
PerformKickState --> Terminate:::terminate : [kickDone]
Terminate:::terminate --> Terminate:::terminate

```

## [PenaltyKickEnemyPlayFSM](/src/software/ai/hl/stp/play/penalty_kick_enemy/penalty_kick_enemy_play_fsm.h)

```mermaid

stateDiagram-v2
classDef terminate fill:white,color:black,font-weight:bold
direction LR
[*] --> SetupPositionState
SetupPositionState --> SetupPositionState : [!setupPositionDone]\n<i>setupPosition</i>
SetupPositionState --> DefendKickState : [setupPositionDone]\n<i>defendKick</i>
DefendKickState --> DefendKickState : <i>defendKick</i>
Terminate:::terminate --> Terminate:::terminate

```

## [ShootOrPassPlayFSM](/src/software/ai/hl/stp/play/shoot_or_pass/shoot_or_pass_play_fsm.h)

```mermaid

stateDiagram-v2
classDef terminate fill:white,color:black,font-weight:bold
direction LR
[*] --> StartState
StartState --> AttemptShotState : <i>startLookingForPass</i>
AttemptShotState --> TakePassState : [passFound]\n<i>takePass</i>
AttemptShotState --> Terminate:::terminate : [tookShot]
AttemptShotState --> AttemptShotState : [!passFound]\n<i>lookForPass</i>
TakePassState --> AttemptShotState : [shouldAbortPass]\n<i>startLookingForPass</i>
TakePassState --> TakePassState : [!passCompleted]\n<i>takePass</i>
TakePassState --> Terminate:::terminate : [passCompleted]\n<i>takePass</i>
Terminate:::terminate --> AttemptShotState : <i>startLookingForPass</i>

```

## [AttackerFSM](/src/software/ai/hl/stp/tactic/attacker/attacker_fsm.h)

```mermaid

stateDiagram-v2
classDef terminate fill:white,color:black,font-weight:bold
direction LR
[*] --> DribbleFSM
DribbleFSM --> PivotKickFSM : [shouldKick]\n<i>pivotKick</i>
DribbleFSM --> KeepAwayFSM : [!shouldKick]\n<i>keepAway</i>
KeepAwayFSM --> PivotKickFSM : [shouldKick]\n<i>pivotKick</i>
KeepAwayFSM --> KeepAwayFSM : <i>keepAway</i>
KeepAwayFSM --> DribbleFSM
PivotKickFSM --> PivotKickFSM : <i>pivotKick</i>
PivotKickFSM --> Terminate:::terminate
Terminate:::terminate --> Terminate:::terminate : <i>SET_STOP_PRIMITIVE_ACTION</i>

```

## [ChipFSM](/src/software/ai/hl/stp/tactic/chip/chip_fsm.h)

```mermaid

stateDiagram-v2
classDef terminate fill:white,color:black,font-weight:bold
direction LR
[*] --> GetBehindBallFSM
GetBehindBallFSM --> GetBehindBallFSM : <i>updateGetBehindBall</i>
GetBehindBallFSM --> ChipState
ChipState --> GetBehindBallFSM : [shouldRealignWithBall]\n<i>updateGetBehindBall</i>
ChipState --> ChipState : [!ballChicked]\n<i>updateChip</i>
ChipState --> Terminate:::terminate : [ballChicked]\n<i>SET_STOP_PRIMITIVE_ACTION</i>
Terminate:::terminate --> Terminate:::terminate : <i>SET_STOP_PRIMITIVE_ACTION</i>

```

## [CreaseDefenderFSM](/src/software/ai/hl/stp/tactic/crease_defender/crease_defender_fsm.h)

```mermaid

stateDiagram-v2
classDef terminate fill:white,color:black,font-weight:bold
direction LR
[*] --> MoveFSM
MoveFSM --> DribbleFSM : [ballNearbyWithoutThreat]\n<i>prepareGetPossession</i>
MoveFSM --> MoveFSM : <i>blockThreat</i>
MoveFSM --> Terminate:::terminate
DribbleFSM --> MoveFSM : [!ballNearbyWithoutThreat]\n<i>blockThreat</i>
DribbleFSM --> DribbleFSM : <i>prepareGetPossession</i>
Terminate:::terminate --> DribbleFSM : [ballNearbyWithoutThreat]\n<i>prepareGetPossession</i>
Terminate:::terminate --> MoveFSM : <i>blockThreat</i>

```

## [DribbleFSM](/src/software/ai/hl/stp/tactic/dribble/dribble_fsm.h)

```mermaid

stateDiagram-v2
classDef terminate fill:white,color:black,font-weight:bold
direction LR
[*] --> GetPossession
GetPossession --> Dribble : [havePossession]\n<i>dribble</i>
GetPossession --> GetPossession : [!havePossession]\n<i>getPossession</i>
Dribble --> LoseBall : [shouldLoseBall]\n<i>loseBall</i>
Dribble --> GetPossession : [lostPossession]\n<i>getPossession</i>
Dribble --> Dribble : [!dribblingDone]\n<i>dribble</i>
Dribble --> Terminate:::terminate : [dribblingDone]\n<i>dribble</i>
LoseBall --> LoseBall : [shouldLoseBall]\n<i>loseBall</i>
LoseBall --> GetPossession : [!shouldLoseBall]\n<i>getPossession</i>
Terminate:::terminate --> GetPossession : [lostPossession]\n<i>getPossession</i>
Terminate:::terminate --> Dribble : [!dribblingDone]\n<i>dribble</i>
Terminate:::terminate --> Terminate:::terminate : <i>dribble</i>

```

## [GetBehindBallFSM](/src/software/ai/hl/stp/tactic/get_behind_ball/get_behind_ball_fsm.h)

```mermaid

stateDiagram-v2
classDef terminate fill:white,color:black,font-weight:bold
direction LR
[*] --> GetBehindBallState
GetBehindBallState --> GetBehindBallState : [!behindBall]\n<i>updateMove</i>
GetBehindBallState --> Terminate:::terminate : [behindBall]\n<i>updateMove</i>
Terminate:::terminate --> GetBehindBallState : [!behindBall]\n<i>updateMove</i>
Terminate:::terminate --> Terminate:::terminate : <i>SET_STOP_PRIMITIVE_ACTION</i>

```

## [GoalieFSM](/src/software/ai/hl/stp/tactic/goalie/goalie_fsm.h)

```mermaid

stateDiagram-v2
classDef terminate fill:white,color:black,font-weight:bold
direction LR
[*] --> PositionToBlock
PositionToBlock --> MoveToGoalLine : [shouldMoveToGoalLine]\n<i>moveToGoalLine</i>
PositionToBlock --> DribbleFSM : [shouldEvacuateCrease]\n<i>retrieveFromDeadZone</i>
PositionToBlock --> Panic : [shouldPanic]\n<i>panic</i>
PositionToBlock --> PivotKickFSM : [shouldPivotChip]\n<i>updatePivotKick</i>
PositionToBlock --> PositionToBlock : <i>positionToBlock</i>
DribbleFSM --> PivotKickFSM : [retrieveDone]\n<i>updatePivotKick</i>
DribbleFSM --> MoveToGoalLine : [shouldMoveToGoalLine]\n<i>moveToGoalLine</i>
DribbleFSM --> DribbleFSM : [ballInInflatedDefenseArea]\n<i>retrieveFromDeadZone</i>
DribbleFSM --> PositionToBlock : [!ballInInflatedDefenseArea]\n<i>positionToBlock</i>
Panic --> MoveToGoalLine : [shouldMoveToGoalLine]\n<i>moveToGoalLine</i>
Panic --> PivotKickFSM : [shouldPivotChip]\n<i>updatePivotKick</i>
Panic --> PositionToBlock : [panicDone]\n<i>positionToBlock</i>
Panic --> Panic : <i>panic</i>
PivotKickFSM --> MoveToGoalLine : [shouldMoveToGoalLine]\n<i>moveToGoalLine</i>
PivotKickFSM --> PivotKickFSM : [ballInInflatedDefenseArea]\n<i>updatePivotKick</i>
PivotKickFSM --> PositionToBlock : [!ballInInflatedDefenseArea]\n<i>positionToBlock</i>
MoveToGoalLine --> MoveToGoalLine : [shouldMoveToGoalLine]\n<i>moveToGoalLine</i>
MoveToGoalLine --> PositionToBlock : [!shouldMoveToGoalLine]\n<i>positionToBlock</i>
Terminate:::terminate --> Terminate:::terminate

```

## [HaltFSM](/src/software/ai/hl/stp/tactic/halt/halt_fsm.h)

```mermaid

stateDiagram-v2
classDef terminate fill:white,color:black,font-weight:bold
direction LR
[*] --> StopState
StopState --> StopState : [!stopDone]\n<i>updateStop</i>
StopState --> Terminate:::terminate : [stopDone]\n<i>updateStop</i>
Terminate:::terminate --> StopState : [!stopDone]\n<i>updateStop</i>
Terminate:::terminate --> Terminate:::terminate : [stopDone]\n<i>updateStop</i>

```

## [KeepAwayFSM](/src/software/ai/hl/stp/tactic/keep_away/keep_away_fsm.h)

```mermaid

stateDiagram-v2
classDef terminate fill:white,color:black,font-weight:bold
direction LR
[*] --> DribbleFSM
DribbleFSM --> DribbleFSM : <i>keepAway</i>
DribbleFSM --> Terminate:::terminate
Terminate:::terminate --> Terminate:::terminate : <i>SET_STOP_PRIMITIVE_ACTION</i>

```

## [KickFSM](/src/software/ai/hl/stp/tactic/kick/kick_fsm.h)

```mermaid

stateDiagram-v2
classDef terminate fill:white,color:black,font-weight:bold
direction LR
[*] --> GetBehindBallFSM
GetBehindBallFSM --> GetBehindBallFSM : <i>updateGetBehindBall</i>
GetBehindBallFSM --> KickState
KickState --> GetBehindBallFSM : [shouldRealignWithBall]\n<i>updateGetBehindBall</i>
KickState --> KickState : [!ballChicked]\n<i>updateKick</i>
KickState --> Terminate:::terminate : [ballChicked]\n<i>SET_STOP_PRIMITIVE_ACTION</i>
Terminate:::terminate --> Terminate:::terminate : <i>SET_STOP_PRIMITIVE_ACTION</i>

```

## [MoveFSM](/src/software/ai/hl/stp/tactic/move/move_fsm.h)

```mermaid

stateDiagram-v2
classDef terminate fill:white,color:black,font-weight:bold
direction LR
[*] --> MoveState
MoveState --> MoveState : [!moveDone]\n<i>updateMove</i>
MoveState --> Terminate:::terminate : [moveDone]\n<i>updateMove</i>
Terminate:::terminate --> MoveState : [!moveDone]\n<i>updateMove</i>
Terminate:::terminate --> Terminate:::terminate : <i>updateMove</i>

```

## [PassDefenderFSM](/src/software/ai/hl/stp/tactic/pass_defender/pass_defender_fsm.h)

```mermaid

stateDiagram-v2
classDef terminate fill:white,color:black,font-weight:bold
direction LR
[*] --> BlockPassState
BlockPassState --> InterceptBallState : [passStarted]\n<i>interceptBall</i>
BlockPassState --> BlockPassState : <i>blockPass</i>
InterceptBallState --> BlockPassState : [ballDeflected]\n<i>blockPass</i>
InterceptBallState --> DribbleFSM : [ballNearbyWithoutThreat]\n<i>prepareGetPossession</i>
DribbleFSM --> BlockPassState : [!ballNearbyWithoutThreat]\n<i>blockPass</i>
DribbleFSM --> DribbleFSM : <i>prepareGetPossession</i>
InterceptBallState --> InterceptBallState : <i>interceptBall</i>
Terminate:::terminate --> Terminate:::terminate : <i>SET_STOP_PRIMITIVE_ACTION</i>

```

## [PenaltyKickFSM](/src/software/ai/hl/stp/tactic/penalty_kick/penalty_kick_fsm.h)

```mermaid

stateDiagram-v2
classDef terminate fill:white,color:black,font-weight:bold
direction LR
[*] --> DribbleFSM
DribbleFSM --> DribbleFSM : [!takePenaltyShot]\n<i>updateApproachKeeper</i>
DribbleFSM --> KickFSM : [timeOutApproach]\n<i>shoot</i>
DribbleFSM --> DribbleFSM : <i>adjustOrientationForShot</i>
DribbleFSM --> KickFSM
KickFSM --> KickFSM : <i>shoot</i>
KickFSM --> Terminate:::terminate
Terminate:::terminate --> Terminate:::terminate : <i>SET_STOP_PRIMITIVE_ACTION</i>

```

## [PivotKickFSM](/src/software/ai/hl/stp/tactic/pivot_kick/pivot_kick_fsm.h)

```mermaid

stateDiagram-v2
classDef terminate fill:white,color:black,font-weight:bold
direction LR
[*] --> StartState
StartState --> DribbleFSM : <i>getPossessionAndPivot</i>
DribbleFSM --> DribbleFSM : <i>getPossessionAndPivot</i>
DribbleFSM --> KickState
KickState --> KickState : [!ballKicked]\n<i>kickBall</i>
KickState --> Terminate:::terminate : [ballKicked]\n<i>SET_STOP_PRIMITIVE_ACTION</i>
Terminate:::terminate --> Terminate:::terminate : <i>SET_STOP_PRIMITIVE_ACTION</i>

```

## [ReceiverFSM](/src/software/ai/hl/stp/tactic/receiver/receiver_fsm.h)

```mermaid

stateDiagram-v2
classDef terminate fill:white,color:black,font-weight:bold
direction LR
[*] --> WaitingForPassState
WaitingForPassState --> WaitingForPassState : [!passStarted]\n<i>updateReceive</i>
WaitingForPassState --> OneTouchShotState : [passStarted && onetouchPossible]\n<i>updateOnetouch</i>
WaitingForPassState --> ReceiveAndDribbleState : [passStarted && !onetouchPossible]\n<i>updateReceive</i>
ReceiveAndDribbleState --> ReceiveAndDribbleState : [!passFinished]\n<i>adjustReceive</i>
OneTouchShotState --> OneTouchShotState : [!passFinished && !strayPass]\n<i>updateOnetouch</i>
OneTouchShotState --> ReceiveAndDribbleState : [!passFinished && strayPass]\n<i>adjustReceive</i>
ReceiveAndDribbleState --> Terminate:::terminate : [passFinished]\n<i>adjustReceive</i>
OneTouchShotState --> Terminate:::terminate : [passFinished]\n<i>updateOnetouch</i>
Terminate:::terminate --> Terminate:::terminate : <i>SET_STOP_PRIMITIVE_ACTION</i>

```

## [ShadowEnemyFSM](/src/software/ai/hl/stp/tactic/shadow_enemy/shadow_enemy_fsm.h)

```mermaid

stateDiagram-v2
classDef terminate fill:white,color:black,font-weight:bold
direction LR
[*] --> MoveFSM
MoveFSM --> BlockPassState : [!enemyThreatHasBall]\n<i>blockPass</i>
MoveFSM --> GoAndStealState : [blockedShot]\n<i>goAndSteal</i>
MoveFSM --> MoveFSM : <i>blockShot</i>
MoveFSM --> GoAndStealState
BlockPassState --> BlockPassState : [!enemyThreatHasBall]\n<i>blockPass</i>
BlockPassState --> MoveFSM : [enemyThreatHasBall]\n<i>blockShot</i>
GoAndStealState --> GoAndStealState : [enemyThreatHasBall && !contestedBall]\n<i>goAndSteal</i>
GoAndStealState --> StealAndPullState : [enemyThreatHasBall && contestedBall]\n<i>goAndSteal</i>
GoAndStealState --> Terminate:::terminate : [!enemyThreatHasBall]\n<i>blockPass</i>
StealAndPullState --> StealAndPullState : [enemyThreatHasBall]\n<i>stealAndPull</i>
StealAndPullState --> Terminate:::terminate : [!enemyThreatHasBall]\n<i>blockPass</i>
Terminate:::terminate --> BlockPassState : [!enemyThreatHasBall]\n<i>blockPass</i>
Terminate:::terminate --> MoveFSM : [enemyThreatHasBall]\n<i>blockShot</i>
Terminate:::terminate --> Terminate:::terminate : <i>SET_STOP_PRIMITIVE_ACTION</i>

```


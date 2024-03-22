import FWCore.ParameterSet.Config as cms

process = cms.Process("Test")

process.source = cms.Source("PoolSource",
  fileNames = cms.untracked.vstring(
    # Multiple file should be comma separated
    # Data set: /DYJetsToLL_M-50_HT-100to200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM
    '/store/mc/RunIIFall17MiniAODv2/DYJetsToLL_M-50_HT-100to200_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/50000/E43E4210-7742-E811-9430-AC1F6B23C96A.root',
  )
)

process.MessageLogger = cms.Service("MessageLogger")
process.maxEvents = cms.untracked.PSet(
  input = cms.untracked.int32(10000)
)

process.analyzeBasicPat = cms.EDAnalyzer("MyZPeakAnalyzer",
  muonSrc = cms.untracked.InputTag("slimmedMuons"),
  elecSrc = cms.untracked.InputTag("slimmedElectrons"),
)

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string('myZPeak.root')
                                   )

process.p = cms.Path(process.analyzeBasicPat)

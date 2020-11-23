#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

"""
 @file ZeroMQCommunicatorRTCTest.py
 @brief ModuleDescription
 @date $Date$


"""
import sys
import time
sys.path.append(".")

# Import RTM module
import RTC
import OpenRTM_aist


# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
zeromqcommunicatorrtctest_spec = ["implementation_id", "ZeroMQCommunicatorRTCTest",
		 "type_name",         "ZeroMQCommunicatorRTCTest",
		 "description",       "ModuleDescription",
		 "version",           "1.0.0",
		 "vendor",            "maruryota",
		 "category",          "Category",
		 "activity_type",     "STATIC",
		 "max_instance",      "1",
		 "language",          "Python",
		 "lang_type",         "SCRIPT",
		 "conf.default.host", "localhost",
		 "conf.default.port", "54323",
		 "conf.default.default_vx", "0",
		 "conf.default.default_vy", "0",
		 "conf.default.default_va", "0",
		 "conf.default.endpoint", "PuffinBP_2",

		 "conf.__widget__.host", "text",
		 "conf.__widget__.port", "text",
		 "conf.__widget__.default_vx", "text",
		 "conf.__widget__.default_vy", "text",
		 "conf.__widget__.default_va", "text",
		 "conf.__widget__.endpoint", "text",

         "conf.__type__.host", "string",
         "conf.__type__.port", "string",
         "conf.__type__.default_vx", "float",
         "conf.__type__.default_vy", "float",
         "conf.__type__.default_va", "float",
         "conf.__type__.endpoint", "string",

		 ""]
# </rtc-template>

##
# @class ZeroMQCommunicatorRTCTest
# @brief ModuleDescription
#
# Communicate to Robot by ZeroMQ.
#
# Input: velocity, Timedvelocity2D
# Output: odometry, TimedPose3D
#
#
class ZeroMQCommunicatorRTCTest(OpenRTM_aist.DataFlowComponentBase):

	##
	# @brief constructor
	# @param manager Maneger Object
	#
	def __init__(self, manager):
		OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

		self._d_odometry = OpenRTM_aist.instantiateDataType(RTC.TimedPose3D)
		"""
		"""
		self._odometryIn = OpenRTM_aist.InPort("odometry", self._d_odometry)
		self._d_velocity = OpenRTM_aist.instantiateDataType(RTC.TimedVelocity2D)
		"""
		"""
		self._velocityOut = OpenRTM_aist.OutPort("velocity", self._d_velocity)





		# initialize of configuration-data.
		# <rtc-template block="init_conf_param">
		"""
		
		 - Name:  host
		 - DefaultValue: localhost
		"""
		self._host = ['localhost']
		"""
		
		 - Name:  port
		 - DefaultValue: 54323
		"""
		self._port = ['54323']
		"""
		
		 - Name:  default_vx
		 - DefaultValue: 0
		"""
		self._default_vx = [0]
		"""
		
		 - Name:  default_vy
		 - DefaultValue: 0
		"""
		self._default_vy = [0]
		"""
		
		 - Name:  default_va
		 - DefaultValue: 0
		"""
		self._default_va = [0]
		"""
		
		 - Name:  endpoint
		 - DefaultValue: PuffinBP_2
		"""
		self._endpoint = ['PuffinBP_2']

		# </rtc-template>



	##
	#
	# The initialize action (on CREATED->ALIVE transition)
	# formaer rtc_init_entry()
	#
	# @return RTC::ReturnCode_t
	#
	#
	def onInitialize(self):
		# Bind variables and configuration variable
		self.bindParameter("host", self._host, "localhost")
		self.bindParameter("port", self._port, "54323")
		self.bindParameter("default_vx", self._default_vx, "0")
		self.bindParameter("default_vy", self._default_vy, "0")
		self.bindParameter("default_va", self._default_va, "0")
		self.bindParameter("endpoint", self._endpoint, "PuffinBP_2")

		# Set InPort buffers
		self.addInPort("odometry",self._odometryIn)

		# Set OutPort buffers
		self.addOutPort("velocity",self._velocityOut)

		# Set service provider to Ports

		# Set service consumers to Ports

		# Set CORBA Service Ports

		return RTC.RTC_OK

	#	##
	#	#
	#	# The finalize action (on ALIVE->END transition)
	#	# formaer rtc_exiting_entry()
	#	#
	#	# @return RTC::ReturnCode_t
	#
	#	#
	#def onFinalize(self):
	#
	#	return RTC.RTC_OK

	#	##
	#	#
	#	# The startup action when ExecutionContext startup
	#	# former rtc_starting_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onStartup(self, ec_id):
	#
	#	return RTC.RTC_OK

	#	##
	#	#
	#	# The shutdown action when ExecutionContext stop
	#	# former rtc_stopping_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onShutdown(self, ec_id):
	#
	#	return RTC.RTC_OK

	#	##
	#	#
	#	# The activated action (Active state entry action)
	#	# former rtc_active_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onActivated(self, ec_id):
	#
	#	return RTC.RTC_OK

	#	##
	#	#
	#	# The deactivated action (Active state exit action)
	#	# former rtc_active_exit()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onDeactivated(self, ec_id):
	#
	#	return RTC.RTC_OK

		##
		#
		# The execution action that is invoked periodically
		# former rtc_active_do()
		#
		# @param ec_id target ExecutionContext Id
		#
		# @return RTC::ReturnCode_t
		#
		#
	def onExecute(self, ec_id):
	
		return RTC.RTC_OK

	#	##
	#	#
	#	# The aborting action when main logic error occurred.
	#	# former rtc_aborting_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onAborting(self, ec_id):
	#
	#	return RTC.RTC_OK

	#	##
	#	#
	#	# The error action in ERROR state
	#	# former rtc_error_do()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onError(self, ec_id):
	#
	#	return RTC.RTC_OK

	#	##
	#	#
	#	# The reset action that is invoked resetting
	#	# This is same but different the former rtc_init_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onReset(self, ec_id):
	#
	#	return RTC.RTC_OK

	#	##
	#	#
	#	# The state update action that is invoked after onExecute() action
	#	# no corresponding operation exists in OpenRTm-aist-0.2.0
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#

	#	#
	#def onStateUpdate(self, ec_id):
	#
	#	return RTC.RTC_OK

	#	##
	#	#
	#	# The action that is invoked when execution context's rate is changed
	#	# no corresponding operation exists in OpenRTm-aist-0.2.0
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onRateChanged(self, ec_id):
	#
	#	return RTC.RTC_OK




def ZeroMQCommunicatorRTCTestInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=zeromqcommunicatorrtctest_spec)
    manager.registerFactory(profile,
                            ZeroMQCommunicatorRTCTest,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    ZeroMQCommunicatorRTCTestInit(manager)

    # Create a component
    comp = manager.createComponent("ZeroMQCommunicatorRTCTest")

def main():
	mgr = OpenRTM_aist.Manager.init(sys.argv)
	mgr.setModuleInitProc(MyModuleInit)
	mgr.activateManager()
	mgr.runManager()

if __name__ == "__main__":
	main()

